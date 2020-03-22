class TopicDiscoverer:

    def __init__(self):
        pass

    def discover(self, vs):
        tfidf_feature_names = vs['tf_vectorizer'].get_feature_names()
        return self.getMostRelevantTopics(vs['lda_tf'], tfidf_feature_names, 10)

    def getMostRelevantTopics(self, model, features, threshold):
        responses = []
        for topic_idx, topic in enumerate(model.components_):
            response = {'title': '', 'terms': [] }
            response['title'] = "Suggested Topic %d" % topic_idx
            response['terms'] = [features[i] for i in topic.argsort()[:-threshold - 1:-1]]
            responses.append(response)
        return responses