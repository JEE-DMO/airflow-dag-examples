

# -----------------------------
# MODELS
# -----------------------------
from .models import (
    AirflowInstance,
    HealthStatus,
)

# -----------------------------
# HEALTH CHECKER
# -----------------------------
from .health_checker import (
    check_all_instances,
    check_instance_health,
    aggregate_health_summary,
    get_instances_from_airflowctl,
)

# -----------------------------
# INSTANCE SOURCES (FACTORY + IMPLS)
# -----------------------------
from .instances_sources import (
    InstanceSource,
    FromAirflowCtlResult,
    FromAirflowCtlCmd,
    FromJsonConfig,
    FromPmsApi,
    get_instance_source,
)

# -----------------------------
# EMAIL + HTML BUILDER
# -----------------------------
from .email_builder import (
    build_environment_details_html,
    build_instance_row_html,
    build_html_report,
    get_email_subject,
)

# -----------------------------
# TASKS (Airflow operators)
# -----------------------------
from .tasks import (
    check_instances,
    generate_report,
    send_report_email,
)

# -----------------------------
# PUBLIC API DU PACKAGE
# -----------------------------
__all__ = [
    # models
    "AirflowInstance",
    "HealthStatus",

    # health checker
    "check_all_instances",
    "check_instance_health",
    "aggregate_health_summary",
    "get_instances_from_airflowctl",

    # instance sources
    "InstanceSource",
    "FromAirflowCtlResult",
    "FromAirflowCtlCmd",
    "FromJsonConfig",
    "FromPmsApi",
    "get_instance_source",

    # email builder
    "build_environment_details_html",
    "build_instance_row_html",
    "build_html_report",
    "get_email_subject",

    # tasks
    "check_instances",
    "generate_report",
    "send_report_email",
]
