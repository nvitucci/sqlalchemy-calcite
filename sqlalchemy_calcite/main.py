import os

from sqlalchemy import create_engine
from sqlalchemy import text


if __name__ == "__main__":
    # Requires to run "mvn package" on calcite-sparql-core first
    jar = "/data/code/git/calcite-sparql/core/target/calcite-sparql-core-0.0.1-SNAPSHOT.jar"

    # The following lines are not always needed, but most of the times they are because
    # the JVM is started without the needed JAR file (see for instance
    # https://github.com/baztian/jaydebeapi/issues/85)
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-1.8.0-openjdk/"
    os.environ["CLASSPATH"] = jar

    conn_string = "/data/code/git/calcite-sparql/examples/java/src/main/resources/modelClassRemote.json"
    dialect = "calcite+jdbc://"
    engine = create_engine(dialect + conn_string)

    query = """
        SELECT w3_label, w3_comment, xmlns_name, xmlns_homepage, xmlns_depiction
        FROM Company
        LIMIT 10
    """

    with engine.connect() as connection:
        result = connection.execute(text(query))
        for row in result:
            print(row)
