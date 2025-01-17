# Blog Django Informatorio - Proyecto Final

## Descripción

Este proyecto corresponde al trabajo final del curso _Informatorio_, donde se diseñó y desarrolló un blog utilizando la tecnología Django. El blog tiene como objetivo difundir, visibilizar y fomentar el debate sobre las iniciativas que contribuyan al cumplimiento de los **17 Objetivos de Desarrollo Sostenible (ODS)** establecidos en la **Agenda 2030 de la ONU**.

El proyecto se ha llevado a cabo de forma grupal, siguiendo los lineamientos del curso, y tiene como propósito reflejar el uso de herramientas y tecnologías aprendidas a lo largo del mismo.

## Objetivos de Desarrollo Sostenible

Los **17 ODS** son un llamado universal para acabar con la pobreza, proteger el planeta y asegurar que todas las personas disfruten de paz y prosperidad para 2030. Estos objetivos fueron adoptados por todos los Estados Miembros de la ONU en 2015 y están diseñados para balancear la sostenibilidad ambiental, económica y social.

En el proyecto, el blog permite la difusión de contenidos que aborden diversos aspectos relacionados con los ODS, con el fin de generar conciencia y promover la acción colectiva para alcanzar estos objetivos ambiciosos.

## Características del Proyecto

- **Acceso de diversos perfiles de usuario**: Los usuarios pueden ser **admin**, **writer** o **reader**, con diferentes permisos:

  - **Admin**: Permite gestionar los posts (CRUD), eliminar comentarios, y ver todos los posts, entre otros privilegios.
  - **Writer**: Permite escribir y comentar posts, pero no eliminar o editar los posts de otros usuarios.
  - **Reader**: Permite solo leer los posts.

- **Gestión de Posts**:

  - Cargar, editar y eliminar posts (solo accesible para el usuario admin).
  - Los posts pueden ser marcados como "En borrador", lo que los hace invisibles para los usuarios hasta ser publicados.
  - Los posts pueden filtrarse por fecha y categoría.
  - Los usuarios pueden ver solo sus propios posts, mientras que el admin puede ver todos los posts.

- **Comentarios**:

  - Los usuarios tipo **writer** pueden comentar los posts.
  - Solo el **admin** tiene permisos para eliminar comentarios.

- **Login**:

  - Los usuarios pueden acceder al sistema con roles de **admin** o **writer**.

- **CRUD implementado**: El sistema de creación, lectura, actualización y eliminación de posts está completamente implementado sin depender solo del sitio de admin.
