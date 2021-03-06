# PyPDB Text Search

## Helpful Links

The Search logic here is a Python wrapper around the RCSB's search logic.
For in-the-weeds details on how each operator works, prefer to look at the
[RCSB Search API documentation](https://search.rcsb.org/index.html)

The search operators defined within the `operators` directory support querying
RCSB attributes against the appropriate `SearchService`. For example, if
you are querying the RCSB Text Search Service (`SearchService.TEXT`), all
operators within `text_operators.py` should be supported.

For a list of RCSB attributes associated with structures you can search, see
[RCSB's List of Attributes to Search](http://search.rcsb.org/search-attributes.html).
Note that not every structure will have every attribute.

Two querying functions are currently supported by PyPDB:

* `perform_search`: This function is good for simple queries
* `perform_search_with_graph`: This function allows building complicated queries using RCSB's query node syntax.

## `perform_search` Examples

### Search for all entries that mention the word 'ribosome'
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.DefaultOperator(value="ribosome")
return_type = ReturnType.ENTRY

results = perform_search(search_service, search_operator, return_type)
```

### Search for polymers from 'Mus musculus'
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.ExactMatchOperator(value="Mus musculus",
                                                    attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
return_type = ReturnType.POLYMER_ENTITY

results = perform_search(search_service, search_operator, return_type)
```

### Search for non-polymers from 'Mus musculus' or 'Homo sapiens'
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_operator = text_operators.InOperator(values=["Mus musculus", "Homo sapiens"],
                                            attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
return_type = ReturnType.NON_POLYMER_ENTITY

results = perform_search(search_service, search_operator, return_type)
```

### Search for polymer instances whose titles contain "actin" or "binding" or "protein"
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.ContainsWordsOperator(value="actin-binding protein",
                                            attribute="struct.title")
return_type = ReturnType.POLYMER_INSTANCE

results = perform_search(search_service, search_operator, return_type)
```

### Search for assemblies that contain the words "actin binding protein"
(must be in that order).

For example, "actin-binding protein" and "actin binding protein" will match,
but "protein binding actin" will not.
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.ContainsPhraseOperator(value="actin-binding protein",
                                            attribute="struct.title")
return_type = ReturnType.ASSEMBLY

results = perform_search(search_service, search_operator, return_type)
```

### Search for entries released in 2019 or later
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.ComparisonOperator(
       value="2019-01-01T00:00:00Z",
       attribute="rcsb_accession_info.initial_release_date",
       comparison_type=text_operators.ComparisonType.GREATER)
return_type = ReturnType.ENTRY

results = perform_search(search_service, search_operator, return_type)
```

### Search for entries released only in 2019 or later
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.RangeOperator(
    from_value="2019-01-01T00:00:00Z",
    to_value="2020-01-01T00:00:00Z",
    include_lower=True,
    include_upper=False,
    attribute="rcsb_accession_info.initial_release_date")
return_type = ReturnType.ENTRY

results = perform_search(search_service, search_operator, return_type)
```
### Search for structures under 4 angstroms of resolution
```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.ComparisonOperator(
           value=4,
           attribute="rcsb_entry_info.resolution_combined",
           comparison_type=text_operators.ComparisonType.LESS)
return_type = ReturnType.ENTRY

results = perform_search(search_service, search_operator, return_type)
```


### Search for structures with a given attribute.

(Admittedly every structure has a release date, but the same logic would
 apply for a more sparse RCSB attribute).

```
from pypdb.clients.search.search_client import perform_search
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.operators import text_operators

search_service = SearchService.TEXT
search_operator = text_operators.ExistsOperator(
    attribute="rcsb_accession_info.initial_release_date")
return_type = ReturnType.ENTRY

results = perform_search(search_service, search_operator, return_type)
```

## `perform_search_with_graph` Example

### Search for 'Mus musculus' or 'Homo sapiens' structures after 2019

```
from pypdb.clients.search.search_client import perform_search_with_graph
from pypdb.clients.search.search_client import SearchService, ReturnType
from pypdb.clients.search.search_client import QueryNode, QueryGroup, LogicalOperator
from pypdb.clients.search.operators import text_operators

# QueryNode associated with structures with under 4 Angstroms of resolution
under_4A_resolution_operator = text_operators.ComparisonOperator(
       value=4,
       attribute="rcsb_entry_info.resolution_combined",
       comparison_type=text_operators.ComparisonType.GREATER)
under_4A_query_node = QueryNode(SearchService.TEXT,
                                  under_4A_resolution_operator)

# QueryNode associated with entities containing 'Mus musculus' lineage
is_mus_operator = text_operators.ExactMatchOperator(
            value="Mus musculus",
            attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
is_mus_query_node = QueryNode(SearchService.TEXT, is_mus_operator)

# QueryNode associated with entities containing 'Homo sapiens' lineage
is_human_operator = text_operators.ExactMatchOperator(
            value="Homo sapiens",
            attribute="rcsb_entity_source_organism.taxonomy_lineage.name")
is_human_query_node = QueryNode(SearchService.TEXT, is_human_operator)

# QueryGroup associated with being either human or `Mus musculus`
is_human_or_mus_group = QueryGroup(
    queries = [is_mus_query_node, is_human_query_node],
    logical_operator = LogicalOperator.OR
)

# QueryGroup associated with being ((Human OR Mus) AND (Under 4 Angstroms))
is_under_4A_and_human_or_mus_group = QueryGroup(
    queries = [is_human_or_mus_group, under_4A_query_node],
    logical_operator = LogicalOperator.AND
)

return_type = ReturnType.ENTRY

results = perform_search_with_graph(
  query_object=is_under_4A_and_human_or_mus_group,
  return_type=return_type)
```
