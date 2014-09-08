import numpy as np
from numpy.random import choice

from utils import write_url_actions, write_url_attributes, get_feat_mat

def generate_url_attr(dictionary, item_ids, topic_size = 10):
    return {id_i : choice(dictionary, topic_size, False) for id_i in item_ids}

def count_similar(A, thresh = .2):
    return np.array([sum(a > thresh)-1.0 for a in A])

def generate_url_actions(urls_attr_prob):
    # impressions
    I = 1000

    # defining a somewhat deterministic set of posibble events
    events = [1, 5, 10, 50, 100, 150]
    click_counts = choice(events, size = 5)
    #click_counts = np.array([10, 1, 10, 10, 200])#testing
    exit_counts = I - np.sum(click_counts)

    c = np.append(click_counts, exit_counts)
    alpha = np.ones(c.shape)
    pi = np.random.dirichlet((c+alpha))
    gamma = pi[-1]

    # how similar is item_i atributes to the other items (proportion)
    #urls_attr_prob = np.array([.01, .1, .01, .01, .1])#testing

    shares_counts = []
    for (clck_counts, clck_prob, attr_prob) in zip(click_counts, pi[:-1], urls_attr_prob):
        share_prob = clck_prob*(1-gamma) + gamma*attr_prob
        shares_counts.append(np.random.binomial(I, share_prob))
    shares_counts = np.array(shares_counts)
    return click_counts, shares_counts

if __name__ == "__main__":
    topic_size = 10
    vocab_size = 50
    num_data_items = 5
    num_test_items = 10

    dictionary = range(vocab_size)
    url_ids = range(num_data_items)

    topics = generate_url_attr(dictionary, url_ids)
    write_url_attributes("./../data/attributes.log", topics)

    map_item_idx = {item_id:idx for idx,item_id in enumerate(topics.iterkeys())}
    map_idx_item = {idx:item_id for item_id,idx in map_item_idx.iteritems()}

    topics_feat_mat = get_feat_mat(topics, map_item_idx, vocab_size)
    # This similarity matrix will be control share counts
    corr = np.dot(topics_feat_mat, topics_feat_mat.T)/topic_size
    share_probs = count_similar(corr)/topic_size

    clicks, shares = generate_url_actions(share_probs)
    write_url_actions("./../data/actions.log", map_idx_item, clicks, shares)

    test_url_ids = range(num_data_items, num_data_items + num_test_items)
    test_topics = generate_url_attr(dictionary, test_url_ids)
    write_url_attributes("./../data/test_attributes.log", test_topics)


