import pkg_resources

from sqlalchemy.dialects import registry

__version__ = pkg_resources.require("sqlalchemy_calcite")[0].version

JDBC_DRIVER_NAME = "org.apache.calcite.avatica.remote.Driver"

registry.register("calcite", "sqlalchemy_calcite.jdbc", "CalciteDialectJdbc")

registry.register("calcite.jdbc", "sqlalchemy_calcite.jdbc", "CalciteDialectJdbc")
