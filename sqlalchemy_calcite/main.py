import os

from sqlalchemy import create_engine
from sqlalchemy.engine.cursor import LegacyCursorResult
from sqlalchemy import text


def run_sparql():
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


def run_mongo():
    # TODO: use cross-OS separator
    os.environ["CLASSPATH"] = ":".join([
        "/Users/nvitucci/Downloads/calcite-core-1.29.0.jar",
        "/Users/nvitucci/Downloads/avatica-core-1.20.0.jar",
        "/Users/nvitucci/Downloads/calcite-linq4j-1.29.0.jar",
        "/Users/nvitucci/Downloads/slf4j-api-1.7.36.jar",
        "/Users/nvitucci/Downloads/protobuf-java-3.19.4.jar",
        "/Users/nvitucci/Downloads/guava-31.1-jre.jar",
        "/Users/nvitucci/Downloads/jackson-databind-2.13.2.jar",
        "/Users/nvitucci/Downloads/jackson-core-2.13.2.jar",
        "/Users/nvitucci/Downloads/jackson-dataformat-yaml-2.13.2.jar",
        "/Users/nvitucci/Downloads/jackson-annotations-2.13.2.jar",
        "/Users/nvitucci/Downloads/json-path-2.7.0.jar",
        "/Users/nvitucci/Downloads/esri-geometry-api-2.2.4.jar",
        "/Users/nvitucci/Downloads/commons-compiler-3.1.6.jar",
        "/Users/nvitucci/Downloads/janino-3.1.6.jar",
        "/Users/nvitucci/Downloads/failureaccess-1.0.1.jar",

        "/Users/nvitucci/Downloads/calcite-mongodb-1.29.0.jar",
        "/Users/nvitucci/Downloads/mongo-java-driver-3.12.10.jar",
    ])

    conn_string = "localhost"
    dialect = "calcite+jdbc://"
    args = {
        "classpath": os.environ["CLASSPATH"],
        "driver_args": {
            "model": "mongo.json",
            "lex": "JAVA"
        }
    }
    engine = create_engine(dialect + conn_string, connect_args=args)

    query = """
        SELECT cast(_MAP['_id'] AS varchar(5)) AS id
        FROM inventory
    """

    with engine.connect() as connection:
        result: LegacyCursorResult = connection.execute(text(query))
        for row in result:
            print(row)


def run_csv():
    # TODO: use cross-OS separator
    os.environ["CLASSPATH"] = ":".join([
        "/Users/nvitucci/Downloads/calcite-core-1.29.0.jar",
        "/Users/nvitucci/Downloads/avatica-core-1.20.0.jar",
        "/Users/nvitucci/Downloads/calcite-linq4j-1.29.0.jar",
        "/Users/nvitucci/Downloads/slf4j-api-1.7.36.jar",
        "/Users/nvitucci/Downloads/protobuf-java-3.19.4.jar",
        "/Users/nvitucci/Downloads/guava-31.1-jre.jar",
        "/Users/nvitucci/Downloads/jackson-databind-2.13.2.jar",
        "/Users/nvitucci/Downloads/jackson-core-2.13.2.jar",
        "/Users/nvitucci/Downloads/jackson-dataformat-yaml-2.13.2.jar",
        "/Users/nvitucci/Downloads/jackson-annotations-2.13.2.jar",
        "/Users/nvitucci/Downloads/json-path-2.7.0.jar",
        "/Users/nvitucci/Downloads/esri-geometry-api-2.2.4.jar",
        "/Users/nvitucci/Downloads/commons-compiler-3.1.6.jar",
        "/Users/nvitucci/Downloads/janino-3.1.6.jar",
        "/Users/nvitucci/Downloads/failureaccess-1.0.1.jar",

        "/Users/nvitucci/Downloads/calcite-example-csv-1.21.0.jar",
        "/Users/nvitucci/Downloads/opencsv-2.3.jar",
        "/Users/nvitucci/Downloads/commons-lang3-3.8.jar",
    ])

    conn_string = "localhost"
    dialect = "calcite+jdbc://"
    args = {
        "classpath": os.environ["CLASSPATH"],
        "driver_args": {
            "model": "csv.json",
            "lex": "JAVA"
        }
    }
    engine = create_engine(dialect + conn_string, connect_args=args)

    query = """
        SELECT *
        FROM example
    """

    with engine.connect() as connection:
        result: LegacyCursorResult = connection.execute(text(query))
        for row in result:
            print(row)


if __name__ == "__main__":
    # The following lines are not always needed, but most of the times they are because
    # the JVM is started without the needed JAR file (see for instance
    # https://github.com/baztian/jaydebeapi/issues/85)
    os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home/"

    # run_sparql()
    # run_mongo()
    run_csv()
