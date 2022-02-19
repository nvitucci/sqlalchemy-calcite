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
        return dbapi2

    def connect(self, *cargs, **cparams):
        args = "-Djava.class.path=%s" % cparams["classpath"]
        jvm_path = jpype.getDefaultJVMPath()
        jpype.startJVM(jvm_path, args)

        return self.dbapi.connect(*cargs, **cparams)

    def initialize(self, connection):
        super(CalciteDialectJdbc, self).initialize(connection)

    def create_connect_args(self, url):
        conn_kwargs = {
            "dsn": "jdbc:calcite:",
            "driver": JDBC_DRIVER_NAME,
        }

        return (), conn_kwargs
