from iwf_api.models import PersistenceLoadingPolicy, PersistenceLoadingType
from iwf_api.models import WorkflowStateOptions as IdlWorkflowStateOptions

from iwf.workflow_state_options import WorkflowStateOptions, _to_idl_state_options


def test_convert_to_idl():
    empty_idl = IdlWorkflowStateOptions()
    assert empty_idl == _to_idl_state_options(None)

    non_empty = WorkflowStateOptions(
        "state-id",
        search_attributes_loading_policy=PersistenceLoadingPolicy(
            persistence_loading_type=PersistenceLoadingType.LOAD_ALL_WITHOUT_LOCKING
        ),
    )
    non_empty_idl = IdlWorkflowStateOptions(
        search_attributes_loading_policy=PersistenceLoadingPolicy(
            persistence_loading_type=PersistenceLoadingType.LOAD_ALL_WITHOUT_LOCKING
        ),
    )
    assert non_empty_idl == _to_idl_state_options(non_empty)
    non_empty.state_id = "state-id-2"
    assert non_empty.state_id == "state-id-2"
