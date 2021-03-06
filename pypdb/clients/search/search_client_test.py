"""Tests for RCSB Search API Python wrapper."""
import json
import requests
import unittest
from unittest import mock

from pypdb.clients.search import search_client
from pypdb.clients.search.operators import text_operators

class TestHTTPRequests(unittest.TestCase):

    @mock.patch.object(requests, "post")
    def test_default_operator_with_entry_return_value(self,
                                                     mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.DefaultOperator(value="ribosome")
        return_type = search_client.ReturnType.ENTRY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
        'query':
            {'type': 'terminal',
             'service': 'text',
             'parameters':
                {'value': 'ribosome'}
            },
        'request_options': {'return_all_hits': True},
        'return_type': 'entry'}

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_exact_match_operator_with_polymer_return(self,
                                                     mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.ExactMatchOperator(value="Mus musculus",
                                                            attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
        return_type = search_client.ReturnType.POLYMER_ENTITY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
        'query':
            {'type': 'terminal',
             'service': 'text',
             'parameters':
                {'attribute': 'rcsb_entity_source_organism.taxonomy_lineage.name',
                'operator': 'exact_match',
                'value': 'Mus musculus'}
            },
        'request_options': {'return_all_hits': True},
        'return_type': 'polymer_entity'}

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_in_operator_with_non_polymer_return(self,
                                                     mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.InOperator(values=["Mus musculus", "Homo sapiens"],
                                                    attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
        return_type = search_client.ReturnType.NON_POLYMER_ENTITY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
        'query':
            {'type': 'terminal',
             'service': 'text',
             'parameters':
                {'attribute': 'rcsb_entity_source_organism.taxonomy_lineage.name',
                'operator': 'in',
                'value': ['Mus musculus', 'Homo sapiens']}
            },
        'request_options': {'return_all_hits': True},
        'return_type': 'non_polymer_entity'}

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_contains_words_operator_with_polymer_instance_return(self,
                                                     mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.ContainsWordsOperator(value="actin-binding protein",
                                                    attribute="struct.title")
        return_type = search_client.ReturnType.POLYMER_INSTANCE

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
        'query':
            {'type': 'terminal',
             'service': 'text',
             'parameters':
                {'attribute': 'struct.title',
                'operator': 'contains_words',
                'value': 'actin-binding protein'}
            },
        'request_options': {'return_all_hits': True},
        'return_type': 'polymer_instance'}

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_contains_phrase_operator_with_assembly_return(self,
                                                     mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.ContainsPhraseOperator(value="actin-binding protein",
                                                    attribute="struct.title")
        return_type = search_client.ReturnType.ASSEMBLY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
        'query':
            {'type': 'terminal',
             'service': 'text',
             'parameters':
                {'attribute': 'struct.title',
                'operator': 'contains_phrase',
                'value': 'actin-binding protein'}
            },
        'request_options': {'return_all_hits': True},
        'return_type': 'assembly'}

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_comparison_operator_with_entry_return(self,
                                                     mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.ComparisonOperator(
               value="2019-01-01T00:00:00Z",
               attribute="rcsb_accession_info.initial_release_date",
               comparison_type=text_operators.ComparisonType.GREATER)
        return_type = search_client.ReturnType.ENTRY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
        'query':
            {'type': 'terminal',
             'service': 'text',
             'parameters':
                {'operator': 'greater',
                'attribute': 'rcsb_accession_info.initial_release_date',
                'value': '2019-01-01T00:00:00Z'}
            },
        'request_options': {'return_all_hits': True},
        'return_type': 'entry'}

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_range_operator_with_entry_return(self, mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.RangeOperator(
            from_value="2019-01-01T00:00:00Z",
            to_value="2019-06-30T00:00:00Z",
            include_lower=False,
            include_upper=True,
            attribute="rcsb_accession_info.initial_release_date")
        return_type = search_client.ReturnType.ENTRY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type)

        expected_json_dict = {
          "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "operator": "range",
              "attribute": "rcsb_accession_info.initial_release_date",
              "value": {
                "from": "2019-01-01T00:00:00Z",
                "to": "2019-06-30T00:00:00Z",
                "include_lower": False,
                "include_upper": True
              }
            }
          },
          "request_options": {"return_all_hits": True},
          "return_type": "entry"
        }

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_exists_operator_with_entry_raw_json_response(self, mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.ExistsOperator(
            attribute="rcsb_accession_info.initial_release_date")
        return_type = search_client.ReturnType.ENTRY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type,
                                     return_raw_json_dict=True)

        expected_json_dict = {
          "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "operator": "exists",
              "attribute": "rcsb_accession_info.initial_release_date",
            }
          },
          "request_options": {"return_all_hits": True},
          "return_type": "entry"
        }

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         canned_json_return_as_dict)

    @mock.patch.object(requests, "post")
    def test_query_group_after_2019_and_either_musculus_or_human(self, mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response

        search_service_one = search_client.SearchService.TEXT
        search_operator_one = text_operators.ComparisonOperator(
               value="2019-01-01T00:00:00Z",
               attribute="rcsb_accession_info.initial_release_date",
               comparison_type=text_operators.ComparisonType.GREATER)
        after_2019_query_node = search_client.QueryNode(
                                    search_service_one, search_operator_one)

        search_service_two = search_client.SearchService.TEXT
        search_operator_two = text_operators.ExactMatchOperator(
                    value="Mus musculus",
                    attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
        is_mus_query_node = search_client.QueryNode(
                                    search_service_two, search_operator_two)

        search_service_three = search_client.SearchService.TEXT
        search_operator_three = text_operators.ExactMatchOperator(
                    value="Homo sapiens",
                    attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
        is_human_query_node = search_client.QueryNode(
                                    search_service_three, search_operator_three)

        is_human_or_mus_group = search_client.QueryGroup(
            queries = [is_mus_query_node, is_human_query_node],
            logical_operator = search_client.LogicalOperator.OR
        )

        is_after_2019_and_human_or_mus_group = search_client.QueryGroup(
            queries = [is_human_or_mus_group, after_2019_query_node],
            logical_operator = search_client.LogicalOperator.AND
        )

        return_type = search_client.ReturnType.ENTRY

        results = search_client.perform_search_with_graph(
        query_object=is_after_2019_and_human_or_mus_group,
                                     return_type=return_type)

        expected_json_dict = {
          "query": {
            "type": "group",
            "logical_operator": "and",
            "nodes": [

                {'type': 'group',
                 'logical_operator': 'or',
                 'nodes': [
                    {
                        'type': 'terminal',
                        'service': 'text',
                        'parameters': {
                            'attribute': 'rcsb_entity_source_organism.taxonomy_lineage.name',
                            'operator': 'exact_match',
                            'value': 'Mus musculus'
                        }
                    },
                    {
                        'type': 'terminal',
                        'service': 'text',
                        'parameters': {
                            'attribute': 'rcsb_entity_source_organism.taxonomy_lineage.name',
                            'operator': 'exact_match',
                            'value': 'Homo sapiens'
                        }
                    },
                 ]
                },
                {'type': 'terminal',
                 'service': 'text',
                 'parameters':
                    {'operator': 'greater',
                    'attribute': 'rcsb_accession_info.initial_release_date',
                    'value': '2019-01-01T00:00:00Z'}
                }
            ]
          },
          "request_options": {"return_all_hits": True},
          "return_type": "entry"
        }

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         ["5JUP", "5JUS", "5JUO"])

    @mock.patch.object(requests, "post")
    def test_query_structure_resolution(self, mock_post):
        # Creates a mock HTTP response, as wrapped by `requests`
        canned_json_return_as_dict = {
            "result_set": [
                {"identifier": "5JUP"},
                {"identifier": "5JUS"},
                {"identifier": "5JUO"}
            ]
        }
        mock_response = mock.create_autospec(requests.Response, instance=True)
        mock_response.json.return_value = canned_json_return_as_dict
        mock_post.return_value = mock_response


        search_service = search_client.SearchService.TEXT
        search_operator = text_operators.ComparisonOperator(
               value=4,
               attribute="rcsb_entry_info.resolution_combined",
               comparison_type=text_operators.ComparisonType.LESS)
        return_type = search_client.ReturnType.ENTRY

        results = search_client.perform_search(search_service,
                                     search_operator,
                                     return_type,
                                     return_raw_json_dict=True)

        expected_json_dict = {
          "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "operator": "less",
              "attribute": "rcsb_entry_info.resolution_combined",
              "value": 4
            }
          },
          "request_options": {"return_all_hits": True},
          "return_type": "entry"
        }

        mock_post.assert_called_once_with(url=search_client.SEARCH_URL_ENDPOINT,
                                          data=json.dumps(expected_json_dict))
        self.assertEqual(results,
                         canned_json_return_as_dict)


if __name__ == '__main__':
    unittest.main()
