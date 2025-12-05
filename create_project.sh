#! /bin/bash

# Verificar que se haya pasado un nombre
if [ $# -lt 2 ]; then
    echo "Uso: ./create_project.sh \"Nombre del Proyecto\""
    echo "  1 = Crear proyecto C#"
    echo "  2 = Crear proyecto Python"
    exit 1
fi
TYPE="$1"
PROJECT_NAME="$2"

# Crear carpeta del proyecto
mkdir "$PROJECT_NAME"
cd "$PROJECT_NAME" || exit 1

########################################
# PROYECTO C#
########################################
create_csharp() {
    # Crea la solución
    dotnet new sln -n "$PROJECT_NAME"

    # Crear la carpeta del proyecto C#
    mkdir "$PROJECT_NAME"

    # Crear el proyecto principal dentro
    dotnet new console -o "$PROJECT_NAME"

    # Agregar el poryecto a la solución
    dotnet sln "$PROJECT_NAME.sln" add "$PROJECT_NAME/$PROJECT_NAME.csproj"

    # Crear test al proyecto
    dotnet new mstest -o tests

    # Agregar los test a la solución
    dotnet sln "$PROJECT_NAME.sln" add "tests/tests.csproj"

    # Referenciamos los el proyecto en los test
    dotnet add "tests/tests.csproj" reference "$PROJECT_NAME/$PROJECT_NAME.csproj"

    echo "Proyecto C# creado correctamente."
}

########################################
# PROYECTO PYTHON
########################################

create_python() {
    # Estructura de directorios
    mkdir -p "$PROJECT_NAME"
    mkdir -p tests

    # Archivos Python
    touch "$PROJECT_NAME/__init__.py"
    touch "$PROJECT_NAME/main.py"
    cat <<EOF > run.py
from $PROJECT_NAME.main import main

if __name__ == "__main__":
    main()

EOF

    touch tests/__init_.py
    cat <<EOF > pytest.ini
[pytest]
pythonpath = .
EOF

    # Requerimientos
    cat <<EOF > requirements.txt
pytest
EOF

    echo "Proyecto Python creado correctamente."
}

########################################

case "$TYPE" in
    1)
        create_csharp
        ;;
    2) 
        create_python
        ;;
    *)
        echo "Tipo inválido. Use 1 (C#) o 2 (Python)."
        exit 1
        ;;
esac

echo "Estructura generada en : $PROJECT_NAME"