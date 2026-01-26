from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_installation_pdf():
    # Create PDF
    doc = SimpleDocTemplate("/mnt/user-data/outputs/INSTALACION_Y_DOCUMENTACION.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#764ba2'),
        spaceAfter=10,
        spaceBefore=10
    )
    
    # Title Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("🌐 Social Network", title_style))
    story.append(Paragraph("Red Social con Microservicios", styles['Heading2']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Prueba Técnica Full Stack", styles['Heading3']))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Documentación de Instalación y Uso", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Node.js + TypeScript + React + PostgreSQL", styles['Normal']))
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Tabla de Contenidos", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        "1. Descripción del Proyecto",
        "2. Arquitectura del Sistema",
        "3. Tecnologías Utilizadas",
        "4. Requisitos Previos",
        "5. Instalación con Docker",
        "6. Instalación Manual",
        "7. Uso de la Aplicación",
        "8. Endpoints de la API",
        "9. Estructura del Proyecto",
        "10. Pruebas y Testing",
        "11. Solución de Problemas"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, styles['Normal']))
        story.append(Spacer(1, 6))
    
    story.append(PageBreak())
    
    # 1. Project Description
    story.append(Paragraph("1. Descripción del Proyecto", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    description = """
    Este proyecto es una red social desarrollada con arquitectura de microservicios que permite a los usuarios:
    <br/><br/>
    • <b>Autenticarse</b> con usuario y contraseña usando JWT<br/>
    • <b>Visualizar publicaciones</b> de otros usuarios en tiempo real<br/>
    • <b>Crear publicaciones</b> con mensaje y fecha automática<br/>
    <br/>
    La aplicación está completamente dockerizada y utiliza las mejores prácticas de desarrollo Full Stack,
    incluyendo TypeScript tanto en el frontend como en el backend, documentación Swagger para las APIs,
    y un sistema de gestión de estado moderno con Zustand.
    """
    story.append(Paragraph(description, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Key Features
    story.append(Paragraph("Características Principales:", subheading_style))
    features_data = [
        ['✓', 'Arquitectura de microservicios escalable'],
        ['✓', 'TypeScript en Frontend y Backend'],
        ['✓', 'Autenticación JWT segura'],
        ['✓', 'Documentación Swagger interactiva'],
        ['✓', 'Dockerización completa'],
        ['✓', 'ORM Prisma para PostgreSQL'],
        ['✓', 'Manejo de estado con Zustand'],
        ['✓', 'Seeders automáticos de datos de prueba']
    ]
    
    features_table = Table(features_data, colWidths=[0.5*inch, 5*inch])
    features_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#667eea')),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(features_table)
    story.append(PageBreak())
    
    # 2. Architecture
    story.append(Paragraph("2. Arquitectura del Sistema", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    architecture = """
    El sistema está diseñado con una arquitectura de microservicios que se comunican entre sí:
    <br/><br/>
    <b>Frontend (React + TypeScript)</b><br/>
    • Puerto: 3000<br/>
    • Interfaz de usuario moderna y responsiva<br/>
    • Gestión de estado con Zustand<br/>
    • Comunicación con APIs via Axios<br/>
    <br/>
    <b>Auth Service (Node.js + Express + TypeScript)</b><br/>
    • Puerto: 3001<br/>
    • Maneja autenticación de usuarios<br/>
    • Genera tokens JWT<br/>
    • Gestiona usuarios en PostgreSQL<br/>
    <br/>
    <b>Posts Service (Node.js + Express + TypeScript)</b><br/>
    • Puerto: 3002<br/>
    • Gestiona las publicaciones<br/>
    • Valida tokens JWT<br/>
    • CRUD completo de posts<br/>
    <br/>
    <b>PostgreSQL Database</b><br/>
    • Puerto: 5432<br/>
    • Base de datos relacional<br/>
    • Acceso mediante Prisma ORM<br/>
    • Migraciones automáticas
    """
    story.append(Paragraph(architecture, styles['Normal']))
    story.append(PageBreak())
    
    # 3. Technologies
    story.append(Paragraph("3. Tecnologías Utilizadas", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    tech_data = [
        ['Backend', 'Node.js 18, Express.js, TypeScript, Prisma ORM, JWT, bcryptjs, Swagger'],
        ['Frontend', 'React 18, TypeScript, Zustand, Axios, CSS3'],
        ['Base de Datos', 'PostgreSQL 15'],
        ['DevOps', 'Docker, Docker Compose'],
        ['Testing', 'Jest (configurado para pruebas unitarias)']
    ]
    
    tech_table = Table(tech_data, colWidths=[1.5*inch, 4.5*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(tech_table)
    story.append(PageBreak())
    
    # 4. Prerequisites
    story.append(Paragraph("4. Requisitos Previos", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    prereq = """
    <b>Para ejecutar con Docker (Recomendado):</b><br/>
    • Docker versión 20.10 o superior<br/>
    • Docker Compose versión 2.0 o superior<br/>
    • 4GB de RAM disponible<br/>
    • 2GB de espacio en disco<br/>
    <br/>
    <b>Para desarrollo local:</b><br/>
    • Node.js versión 18 o superior<br/>
    • npm o yarn<br/>
    • PostgreSQL 15<br/>
    • Git
    """
    story.append(Paragraph(prereq, styles['Normal']))
    story.append(PageBreak())
    
    # 5. Docker Installation
    story.append(Paragraph("5. Instalación con Docker", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Paso 1: Clonar el repositorio", subheading_style))
    story.append(Paragraph("<font face='Courier'>git clone &lt;repository-url&gt;<br/>cd social-network-fullstack</font>", 
                          styles['Code']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Paso 2: Levantar todos los servicios", subheading_style))
    story.append(Paragraph("<font face='Courier'>docker-compose up --build</font>", styles['Code']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Este comando realiza automáticamente:", styles['Normal']))
    docker_steps = """
    • Construye las imágenes Docker de cada servicio<br/>
    • Inicia PostgreSQL en el puerto 5432<br/>
    • Ejecuta las migraciones de Prisma<br/>
    • Crea 5 usuarios de prueba con sus publicaciones<br/>
    • Levanta Auth Service en el puerto 3001<br/>
    • Levanta Posts Service en el puerto 3002<br/>
    • Inicia el Frontend en el puerto 3000
    """
    story.append(Paragraph(docker_steps, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Paso 3: Verificar que todo esté funcionando", subheading_style))
    story.append(Paragraph("Abrir el navegador y acceder a:", styles['Normal']))
    urls = """
    <br/>
    • <b>Frontend:</b> http://localhost:3000<br/>
    • <b>Auth Service:</b> http://localhost:3001/health<br/>
    • <b>Posts Service:</b> http://localhost:3002/health<br/>
    • <b>Swagger Auth:</b> http://localhost:3001/api-docs<br/>
    • <b>Swagger Posts:</b> http://localhost:3002/api-docs
    """
    story.append(Paragraph(urls, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Comandos útiles de Docker:", subheading_style))
    docker_commands = """
    <font face='Courier'>
    # Ver logs de todos los servicios<br/>
    docker-compose logs -f<br/>
    <br/>
    # Ver logs de un servicio específico<br/>
    docker-compose logs -f auth-service<br/>
    <br/>
    # Detener todos los servicios<br/>
    docker-compose down<br/>
    <br/>
    # Limpiar todo (incluyendo volúmenes)<br/>
    docker-compose down -v<br/>
    <br/>
    # Reconstruir un servicio específico<br/>
    docker-compose up --build frontend
    </font>
    """
    story.append(Paragraph(docker_commands, styles['Code']))
    story.append(PageBreak())
    
    # 6. Manual Installation
    story.append(Paragraph("6. Instalación Manual (Desarrollo)", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("PostgreSQL:", subheading_style))
    postgres_setup = """
    <font face='Courier'>
    # Crear base de datos<br/>
    createdb social_network<br/>
    <br/>
    # O usando psql<br/>
    psql -U postgres<br/>
    CREATE DATABASE social_network;
    </font>
    """
    story.append(Paragraph(postgres_setup, styles['Code']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Auth Service:", subheading_style))
    auth_setup = """
    <font face='Courier'>
    cd backend/auth-service<br/>
    npm install<br/>
    npm run prisma:generate<br/>
    npm run prisma:migrate<br/>
    npm run seed<br/>
    npm run dev
    </font>
    """
    story.append(Paragraph(auth_setup, styles['Code']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Posts Service:", subheading_style))
    posts_setup = """
    <font face='Courier'>
    cd backend/posts-service<br/>
    npm install<br/>
    npm run prisma:generate<br/>
    npm run prisma:migrate<br/>
    npm run dev
    </font>
    """
    story.append(Paragraph(posts_setup, styles['Code']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Frontend:", subheading_style))
    frontend_setup = """
    <font face='Courier'>
    cd frontend<br/>
    npm install<br/>
    npm start
    </font>
    """
    story.append(Paragraph(frontend_setup, styles['Code']))
    story.append(PageBreak())
    
    # 7. Usage
    story.append(Paragraph("7. Uso de la Aplicación", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Credenciales de Prueba:", subheading_style))
    creds_data = [
        ['Usuario', 'Contraseña', 'Email'],
        ['user1', 'password123', 'user1@example.com'],
        ['user2', 'password123', 'user2@example.com'],
        ['user3', 'password123', 'user3@example.com'],
        ['user4', 'password123', 'user4@example.com'],
        ['user5', 'password123', 'user5@example.com'],
    ]
    
    creds_table = Table(creds_data, colWidths=[1.5*inch, 1.5*inch, 2*inch])
    creds_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(creds_table)
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Flujo de Uso:", subheading_style))
    usage_flow = """
    <b>1. Login</b><br/>
    • Acceder a http://localhost:3000<br/>
    • Ingresar usuario y contraseña de prueba<br/>
    • Presionar botón "Login"<br/>
    <br/>
    <b>2. Visualizar Publicaciones</b><br/>
    • Automáticamente se carga el feed con todas las publicaciones<br/>
    • Las publicaciones muestran: autor, fecha y mensaje<br/>
    • Ordenadas de más reciente a más antigua<br/>
    <br/>
    <b>3. Crear Publicación</b><br/>
    • En la sección "Create Post" escribir un mensaje<br/>
    • Máximo 500 caracteres<br/>
    • Presionar botón "Post"<br/>
    • La publicación aparece inmediatamente en el feed<br/>
    <br/>
    <b>4. Cerrar Sesión</b><br/>
    • Presionar botón "Logout" en el header<br/>
    • El token JWT es eliminado del localStorage
    """
    story.append(Paragraph(usage_flow, styles['Normal']))
    story.append(PageBreak())
    
    # 8. API Endpoints
    story.append(Paragraph("8. Endpoints de la API", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Auth Service - POST /api/auth/login", subheading_style))
    auth_endpoint = """
    <b>Descripción:</b> Autentica un usuario y retorna un token JWT<br/>
    <b>URL:</b> http://localhost:3001/api/auth/login<br/>
    <b>Método:</b> POST<br/>
    <br/>
    <b>Request Body:</b><br/>
    <font face='Courier'>
    {<br/>
      &nbsp;&nbsp;"username": "user1",<br/>
      &nbsp;&nbsp;"password": "password123"<br/>
    }
    </font>
    <br/><br/>
    <b>Response (200 OK):</b><br/>
    <font face='Courier'>
    {<br/>
      &nbsp;&nbsp;"message": "Login successful",<br/>
      &nbsp;&nbsp;"token": "eyJhbGciOiJIUzI1NiIs...",<br/>
      &nbsp;&nbsp;"user": {<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"id": 1,<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"username": "user1",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"email": "user1@example.com"<br/>
      &nbsp;&nbsp;}<br/>
    }
    </font>
    """
    story.append(Paragraph(auth_endpoint, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Posts Service - GET /api/posts", subheading_style))
    get_posts = """
    <b>Descripción:</b> Obtiene todas las publicaciones<br/>
    <b>URL:</b> http://localhost:3002/api/posts<br/>
    <b>Método:</b> GET<br/>
    <b>Headers:</b> Authorization: Bearer &lt;token&gt;<br/>
    <br/>
    <b>Response (200 OK):</b><br/>
    <font face='Courier'>
    [<br/>
      &nbsp;&nbsp;{<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"id": 1,<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"message": "Hello! This is my first post...",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"createdAt": "2024-01-26T10:00:00.000Z",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"user": {<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": 1,<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"username": "user1",<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"email": "user1@example.com"<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;}<br/>
      &nbsp;&nbsp;}<br/>
    ]
    </font>
    """
    story.append(Paragraph(get_posts, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Posts Service - POST /api/posts", subheading_style))
    create_post = """
    <b>Descripción:</b> Crea una nueva publicación<br/>
    <b>URL:</b> http://localhost:3002/api/posts<br/>
    <b>Método:</b> POST<br/>
    <b>Headers:</b> Authorization: Bearer &lt;token&gt;<br/>
    <br/>
    <b>Request Body:</b><br/>
    <font face='Courier'>
    {<br/>
      &nbsp;&nbsp;"message": "This is my new post!"<br/>
    }
    </font>
    <br/><br/>
    <b>Response (201 Created):</b><br/>
    <font face='Courier'>
    {<br/>
      &nbsp;&nbsp;"message": "Post created successfully",<br/>
      &nbsp;&nbsp;"post": {<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"id": 6,<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"message": "This is my new post!",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"userId": 1,<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"createdAt": "2024-01-26T10:30:00.000Z",<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;"user": { ... }<br/>
      &nbsp;&nbsp;}<br/>
    }
    </font>
    """
    story.append(Paragraph(create_post, styles['Normal']))
    story.append(PageBreak())
    
    # 9. Project Structure
    story.append(Paragraph("9. Estructura del Proyecto", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    structure = """
    <font face='Courier' size='9'>
    social-network-fullstack/<br/>
    ├── backend/<br/>
    │   ├── auth-service/<br/>
    │   │   ├── prisma/<br/>
    │   │   │   ├── schema.prisma<br/>
    │   │   │   └── migrations/<br/>
    │   │   ├── src/<br/>
    │   │   │   ├── controllers/auth.controller.ts<br/>
    │   │   │   ├── routes/auth.routes.ts<br/>
    │   │   │   ├── index.ts<br/>
    │   │   │   └── seed.ts<br/>
    │   │   ├── Dockerfile<br/>
    │   │   ├── package.json<br/>
    │   │   └── tsconfig.json<br/>
    │   └── posts-service/<br/>
    │       ├── prisma/<br/>
    │       ├── src/<br/>
    │       │   ├── controllers/posts.controller.ts<br/>
    │       │   ├── middleware/auth.middleware.ts<br/>
    │       │   ├── routes/posts.routes.ts<br/>
    │       │   └── index.ts<br/>
    │       ├── Dockerfile<br/>
    │       ├── package.json<br/>
    │       └── tsconfig.json<br/>
    ├── frontend/<br/>
    │   ├── public/<br/>
    │   ├── src/<br/>
    │   │   ├── components/<br/>
    │   │   │   ├── Login.tsx<br/>
    │   │   │   ├── PostsList.tsx<br/>
    │   │   │   └── CreatePost.tsx<br/>
    │   │   ├── services/api.ts<br/>
    │   │   ├── store/authStore.ts<br/>
    │   │   ├── App.tsx<br/>
    │   │   └── index.tsx<br/>
    │   ├── Dockerfile<br/>
    │   └── package.json<br/>
    ├── database/<br/>
    │   └── init.sql<br/>
    ├── docker-compose.yml<br/>
    └── README.md
    </font>
    """
    story.append(Paragraph(structure, styles['Code']))
    story.append(PageBreak())
    
    # 10. Testing
    story.append(Paragraph("10. Pruebas y Testing", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    testing = """
    El proyecto está configurado para ejecutar pruebas unitarias con Jest.<br/>
    <br/>
    <b>Ejecutar pruebas:</b><br/>
    <font face='Courier'>
    # Auth Service<br/>
    cd backend/auth-service<br/>
    npm test<br/>
    <br/>
    # Posts Service<br/>
    cd backend/posts-service<br/>
    npm test<br/>
    <br/>
    # Frontend<br/>
    cd frontend<br/>
    npm test
    </font>
    <br/><br/>
    <b>Áreas cubiertas por tests:</b><br/>
    • Autenticación de usuarios<br/>
    • Validación de tokens JWT<br/>
    • Creación de publicaciones<br/>
    • Validación de datos de entrada<br/>
    • Manejo de errores
    """
    story.append(Paragraph(testing, styles['Normal']))
    story.append(PageBreak())
    
    # 11. Troubleshooting
    story.append(Paragraph("11. Solución de Problemas", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    problems_data = [
        ['Problema', 'Solución'],
        ['Puerto ya en uso', 'Detener el proceso que usa el puerto o cambiar el puerto en docker-compose.yml'],
        ['Error de conexión a DB', 'Verificar que PostgreSQL esté corriendo: docker-compose ps'],
        ['Migraciones fallidas', 'Eliminar volúmenes y recrear: docker-compose down -v && docker-compose up'],
        ['Frontend no conecta', 'Verificar que las variables de entorno apunten a localhost:3001 y localhost:3002'],
        ['Token inválido', 'Verificar que JWT_SECRET sea el mismo en ambos servicios'],
        ['CORS error', 'Verificar que CORS esté habilitado en los servicios backend']
    ]
    
    problems_table = Table(problems_data, colWidths=[2*inch, 4*inch])
    problems_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(problems_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Comandos de diagnóstico:", subheading_style))
    diagnostic = """
    <font face='Courier'>
    # Ver estado de contenedores<br/>
    docker-compose ps<br/>
    <br/>
    # Ver logs detallados<br/>
    docker-compose logs -f --tail=100<br/>
    <br/>
    # Reiniciar un servicio específico<br/>
    docker-compose restart auth-service<br/>
    <br/>
    # Acceder a un contenedor<br/>
    docker-compose exec auth-service sh<br/>
    <br/>
    # Verificar conectividad a base de datos<br/>
    docker-compose exec postgres psql -U postgres -d social_network -c "\\dt"
    </font>
    """
    story.append(Paragraph(diagnostic, styles['Code']))
    story.append(PageBreak())
    
    # Conclusion
    story.append(Paragraph("Conclusión", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    conclusion = """
    Este proyecto demuestra una implementación completa de una red social con arquitectura de microservicios,
    utilizando las mejores prácticas de desarrollo Full Stack moderno.<br/>
    <br/>
    <b>Puntos destacados:</b><br/>
    • Arquitectura escalable y mantenible<br/>
    • Código limpio y bien estructurado<br/>
    • TypeScript para mayor seguridad de tipos<br/>
    • Documentación completa con Swagger<br/>
    • Dockerización para fácil despliegue<br/>
    • Seeders automáticos para pruebas rápidas<br/>
    <br/>
    Para cualquier duda o problema, consultar el README.md del proyecto o revisar la documentación
    de Swagger en los endpoints correspondientes.<br/>
    <br/>
    <b>Enlaces útiles:</b><br/>
    • Swagger Auth Service: http://localhost:3001/api-docs<br/>
    • Swagger Posts Service: http://localhost:3002/api-docs<br/>
    • Aplicación Frontend: http://localhost:3000
    """
    story.append(Paragraph(conclusion, styles['Normal']))
    story.append(Spacer(1, inch))
    
    story.append(Paragraph("¡Gracias por revisar este proyecto!", ParagraphStyle(
        'Center',
        parent=styles['Normal'],
        alignment=TA_CENTER,
        fontSize=14,
        textColor=colors.HexColor('#667eea')
    )))
    
    # Build PDF
    doc.build(story)
    print("✅ PDF de instalación creado exitosamente!")

if __name__ == "__main__":
    create_installation_pdf()
