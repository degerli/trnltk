import itertools
from trnltk.morphology.model import formatter

class StatisticalParseResult(object):
    def __init__(self):
        self.parse_result_occurrences = dict()
        self.parse_results = dict()

    def add_parse_result(self, contextless_parse_result, offsets):
        parse_result_str = formatter.format_morpheme_container_for_parseset(contextless_parse_result)
        self.parse_results[parse_result_str] = contextless_parse_result
        self.parse_result_occurrences[parse_result_str] = offsets

    # TODO: better naming is normalizing, probability
    def get_parse_results_with_ratio(self):
        results_with_ratio = []
        total_occurrence = float(sum(itertools.chain.from_iterable(self.parse_result_occurrences.itervalues())))
        for parse_result_str in self.parse_result_occurrences.iterkeys():
            occurrence_of_parse_result = float(len(self.parse_result_occurrences[parse_result_str]))
            ratio = occurrence_of_parse_result / total_occurrence
            results_with_ratio.append((parse_result_str, ratio))

        return results_with_ratio

class StatisticalParser(object):
    def __init__(self, contextless_parser, parse_result_concordance_index):
        self.contextless_parser = contextless_parser
        self._parse_result_concordance_index = parse_result_concordance_index

    def parse(self, word_str):
        contextless_parse_results = self.contextless_parser.parse(word_str)
        statistical_parse_result = StatisticalParseResult()
        for contextless_parse_result in contextless_parse_results:
            offsets_for_same_parse_result = self._parse_result_concordance_index.offsets(word_str)
            statistical_parse_result.add_parse_result(contextless_parse_result, offsets_for_same_parse_result)

        return statistical_parse_result

