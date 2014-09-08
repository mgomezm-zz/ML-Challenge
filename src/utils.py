import numpy as np
from numpy.random import choice

def write_url_actions(filename, map_idx_item, clicks, shares):
    with open(filename, 'w') as fd_w:
        for idx, c in enumerate(clicks):
            for _ in xrange(c):
                fd_w.write("pageview"+"\t"+"http://foo.com/" + str(map_idx_item[idx])+"\n")

        for idx, s in enumerate(shares):
            for _ in xrange(s):
                fd_w.write("share"+"\t"+"http://foo.com/" + str(map_idx_item[idx])+"\n")

def write_url_attributes(filename, topics):
    with open(filename, 'w') as fd_w:
        for item, x in topics.iteritems():
            print>>fd_w, "http://foo.com/" + str(item)+"\t", x

def read_url_actions(filename):
    clicks = {}
    shares = {}
    with open(filename, 'r') as fd_r:
        for line in fd_r:
            action, url = line.strip().split('\t')
            item_id = int(url.split('/')[-1])
            if action == "pageview":
                clicks[item_id] = clicks.get(item_id, 0) + 1
            elif action == "share":
                shares[item_id] = shares.get(item_id, 0) + 1
    return clicks, shares

def read_url_attributes(filename):
    test_attr = {}
    with open(filename, 'r') as fd_r:
        for line in fd_r:
            url, attr = line.strip().split('\t')
            attr = attr.lstrip('[')
            attr = attr.rstrip(']')
            attr = map(int, attr.split())
            item_id = int(url.split('/')[-1])
            test_attr[item_id] = attr
    return test_attr


def get_feat_mat(attr, map_item_idx, vocab_size):
    num_items = len(attr)
    feat_mat = np.zeros((num_items, vocab_size))
    for item_id, topics in attr.iteritems():
        topics_idx = np.array(topics)
        feat_mat[map_item_idx[item_id], topics_idx] = 1
    return feat_mat
