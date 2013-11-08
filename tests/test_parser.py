# coding: utf-8

import os
from writeup import parser
from nose.tools import raises
dirname = os.path.abspath(os.path.dirname(__file__))


def test_parse_meta():
    text = '\n'.join([
        '# title',
        '- key: value',
        '- url: http://lepture.com',
        '',
        'A description about essay up.',
    ])
    meta = parser.parse_meta(text)
    assert u'title' == meta['title']
    assert u'value' == meta['key']
    assert u'http://lepture.com' == meta['url']
    assert u'A description about essay up.' == meta['description']


def test_parse_meta_no_title():
    text = '\n'.join([
        'spam',
        '# title',
        '- key: value',
        '- url: http://lepture.com',
        '',
        'A description about essay up.',
    ])
    meta = parser.parse_meta(text)
    assert meta['title'] is None


def test_parse():
    text = '\n'.join([
        '# title',
        '- key: value',
        '- url: http://lepture.com',
        '',
        'A description about essay up.',
        '-------',
        '',
        'A content placeholder.',
    ])
    meta, body = parser.parse(text)
    assert meta['title'] == u'title'


def test_read():
    f = os.path.join(dirname, 'cases', 'parser', 'welcome-to-writeup.md')
    post = parser.read(f, postsdir=dirname)
    assert post.title == u'Welcome to Writeup'
    assert post.filename == u'welcome-to-writeup'
    assert post.dirname == u'cases/parser'
    assert post.url == u'/2013/welcome-to-writeup.html'
    assert post.id == u'cases-parser-welcome-to-writeup'


@raises(RuntimeError)
def test_no_source():
    f = os.path.join(dirname, 'cases', 'parser', 'welcome-to-writeup.md')
    post = parser.read(f)
    assert post.dirname == u'cases/parser'
