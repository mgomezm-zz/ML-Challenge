import numpy as np

from utils import read_url_actions, read_url_attributes, get_feat_mat

def sim_recommender(id_clicks, id_shares, topics, test_topics, vocab_size, topic_size):
    #preprocessing
    num_data_items = len(id_clicks)
    num_test_items = len(test_topics)

    map_item_idx = {item_id:idx for idx,item_id in enumerate(topics.iterkeys())}
    map_idx_item = {idx:item_id for item_id,idx in map_item_idx.iteritems()}

    map_testitem_idx = {item_id:idx for idx,item_id in enumerate(test_topics.iterkeys())}
    map_idx_testitem = {idx:item_id for item_id,idx in map_testitem_idx.iteritems()}

    topics_feat_mat = get_feat_mat(topics, map_item_idx, vocab_size)
    testtopics_feat_mat = get_feat_mat(test_topics, map_testitem_idx, vocab_size)

    clicks = np.array([id_clicks[map_idx_item[idx]] for idx in range(num_data_items)])
    shares = np.array([id_shares[map_idx_item[idx]] for idx in range(num_data_items)])

    # recommender based on weighted cosine similarity
    # alpha controls the importance on page views and share counts
    alpha = .2
    weigthed_topics_mat = topics_feat_mat*(alpha*clicks.reshape((num_data_items,1)) +
                                (1-alpha)*shares.reshape((num_data_items,1)))

    corr = np.dot(testtopics_feat_mat, topics_feat_mat.T)/topic_size
    sim = np.dot(testtopics_feat_mat, weigthed_topics_mat.T)

    max_idx = np.argmax(sim)
    best_test_item = max_idx/num_test_items
    most_similar_item = max_idx%num_data_items

    print "".join(['=']*80)
    print "Out of the 10 items in the test.log, the item that should be sent is", map_idx_testitem[best_test_item]
    print "Its is most similar to item", map_idx_item[most_similar_item]
    print "With a imilarity of ", corr[best_test_item, most_similar_item]
    print "Number of page views ", clicks[most_similar_item]
    print "Number of shares", shares[most_similar_item]

if __name__ == "__main__":
    vocab_size = 50
    topic_size = 10

    id_clicks, id_shares = read_url_actions("./../data/actions.log")
    topics = read_url_attributes("./../data/attributes.log")
    test_topics = read_url_attributes("./../data/test_attributes.log")

    sim_recommender(id_clicks, id_shares, topics, test_topics, vocab_size, topic_size)
