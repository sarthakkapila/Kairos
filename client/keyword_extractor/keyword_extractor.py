from keybert import KeyBERT

class SentenceBert:
    def __init__(self):
        self.kw_model = KeyBERT()

    def extract_keywords(self, sentence, top_n: int = 5) -> list:
        """
        Extracts keywords from a given sentence using BERT embeddings.

        Args:
            sentence (str): The input sentence from which keywords are to be extracted.
            top_n (int): The number of top keywords to be extracted. Default is 5.

        Returns:
            list: A list of extracted keywords.
        """
        if not sentence:
            return []

        try:
            keywords = self.kw_model.extract_keywords(
                sentence,
                keyphrase_ngram_range=(1, 1),
                stop_words="english",
                top_n=top_n,
                use_mmr=True,
                diversity=0.7,
            )

            keywords = [word[0] for word in keywords]

            return keywords

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
