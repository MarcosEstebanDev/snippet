# Respositorio django snippets

Aplicación en la cual usuarios registrados pueden crear Snippets de código en diferentes
lenguajes de programación.

## Desarrollo del Proyecto

Este proyecto fue desarrollado utilizando el framework Django. A continuación, se detallan los pasos principales:

1. **Configuración del entorno**: Se creó un entorno virtual y se instalaron las dependencias necesarias.
2. **Creación de la aplicación**: Se generó una nueva aplicación Django para manejar los snippets.
3. **Modelado de datos**: Se definieron los modelos para los snippets y los usuarios.
4. **Vistas y URLs**: Se implementaron las vistas y las rutas para crear, editar y visualizar snippets.
5. **Autenticación**: Se configuró el sistema de autenticación para que solo los usuarios registrados puedan crear y editar snippets.
6. **Interfaz de usuario**: Se diseñó una interfaz sencilla y funcional utilizando HTML, CSS y Bootstrap.
   - **CSS**: Se utilizó CSS para personalizar el estilo de la aplicación y mejorar la experiencia del usuario.
   - **Bootstrap**: Se integró Bootstrap para aprovechar sus componentes y utilidades de diseño responsivo.
7. **Pygments**: Se utilizó Pygments para resaltar la sintaxis de los snippets de código, mejorando la legibilidad y presentación.
8. **Pruebas**: Se realizaron pruebas para asegurar el correcto funcionamiento de la aplicación.

## Flujo de la Aplicación

1. **Inicio de sesión**: Los usuarios deben registrarse e iniciar sesión para poder crear, editar y eliminar snippets.
2. **Creación de snippets**: Una vez autenticados, los usuarios pueden crear nuevos snippets proporcionando el título, el lenguaje de programación y el código.
3. **Edición de snippets**: Los usuarios pueden editar sus propios snippets en cualquier momento.
4. **Eliminación de snippets**: Los usuarios pueden eliminar sus propios snippets si ya no los necesitan.
5. **Privacidad de los snippets**: 
   - Los snippets pueden ser públicos o privados.
   - Los snippets públicos son visibles para todos los usuarios.
   - Los snippets privados solo son visibles para el usuario que los creó.