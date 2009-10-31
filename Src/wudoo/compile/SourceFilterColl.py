from wudoo.filter.AcceptAllFilter import AcceptAllFilter
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter

CPP_SOURCE_FILTER = ExtensionBasedFilter({"cpp": "cpp"})
HDR_SOURCE_FILTER = ExtensionBasedFilter({"h": "h"})
ACCEPT_ALL_FILTER = AcceptAllFilter()
