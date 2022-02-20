from sqlalchemy.engine.default import DefaultDialect


class CalciteDialect(DefaultDialect):
    # Start abstract methods

    def get_columns(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def get_table_names(self, connection, schema=None, **kw):
        raise NotImplementedError()

    def get_temp_table_names(self, connection, schema=None, **kw):
        raise NotImplementedError()

    def get_view_names(self, connection, schema=None, **kw):
        raise NotImplementedError()

    def get_sequence_names(self, connection, schema=None, **kw):
        raise NotImplementedError()

    def get_temp_view_names(self, connection, schema=None, **kw):
        raise NotImplementedError()

    def get_view_definition(self, connection, view_name, schema=None, **kw):
        raise NotImplementedError()

    def get_indexes(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def get_unique_constraints(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def get_check_constraints(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def get_table_comment(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def has_table(self, connection, table_name, schema=None, **kw):
        raise NotImplementedError()

    def has_sequence(self, connection, sequence_name, schema=None, **kw):
        raise NotImplementedError()

    def _get_server_version_info(self, connection):
        raise NotImplementedError()

    def _get_default_schema_name(self, connection):
        raise NotImplementedError()

    def do_set_input_sizes(self, cursor, list_of_tuples, context):
        raise NotImplementedError()

    def do_begin_twophase(self, connection, xid):
        raise NotImplementedError()

    def do_prepare_twophase(self, connection, xid):
        raise NotImplementedError()

    def do_rollback_twophase(self, connection, xid, is_prepared=True, recover=False):
        raise NotImplementedError()

    def do_commit_twophase(self, connection, xid, is_prepared=True, recover=False):
        raise NotImplementedError()

    def do_recover_twophase(self, connection):
        raise NotImplementedError()

    def set_isolation_level(self, dbapi_conn, level):
        raise NotImplementedError()

    def get_isolation_level(self, dbapi_conn):
        raise NotImplementedError()

    # End abstract methods

    # This is necessary to prevent a rollback exception to be called
    def do_rollback(self, dbapi_connection):
        pass
