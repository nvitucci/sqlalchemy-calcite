import os

from sqlalchemy import create_engine
from sqlalchemy import text


if __name__ == "__main__":
    # The following lines are not always needed, but most of the times they are because
    # the JVM is started without the needed JAR file (see for instance
    # https://github.com/baztian/jaydebeapi/issues/85)
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-1.8.0-openjdk/"

    conn_string = "localhost"
    dialect = "calcite+jdbc://"
    args = {
        "classpath": os.environ["CLASSPATH"],
        "driver_args": {
            "model": "modelClassRemote.json",
            "lex": "JAVA"
        }
    }
    engine = create_engine(dialect + conn_string, connect_args=args)

    query = """
        SELECT w3_label, w3_comment, xmlns_name, xmlns_homepage, xmlns_depiction
        FROM Company
        LIMIT 10
    """

    with engine.connect() as connection:
        result = connection.execute(text(query))
        for row in result:
            print(row)
