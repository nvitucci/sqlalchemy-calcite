import os

import jpype

from jpype import dbapi2

from sqlalchemy_calcite import JDBC_DRIVER_NAME
from sqlalchemy_calcite.base import CalciteDialect


class CalciteDialectJdbc(CalciteDialect):
    driver = "jdbc"
    supports_statement_cache = True

    @classmethod
    def dbapi(cls):
        args = "-Djava.class.path=%s" % os.environ["CLASSPATH"]
        jvm_path = jpype.getDefaultJVMPath()
        jpype.startJVM(jvm_path, args)

        return dbapi2

    def initialize(self, connection):
        super(CalciteDialectJdbc, self).initialize(connection)

    def create_connect_args(self, url):
        model_path = str(url).split("://", 1)[1]

        kwargs = {
            "dsn": "jdbc:calcite:",
            "driver": JDBC_DRIVER_NAME,
            "driver_args": {
                "model": model_path,
                "lex": "JAVA"
            },
        }

        return (), kwargs
