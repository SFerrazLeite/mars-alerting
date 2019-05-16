java -- Spring Boot
===================

Run ```./gradlew build``` on Linux like systems or ```gradlew.bat build``` on Windows to compile your application.
Then, run ```java -jar build\libs\mars-alerting-1.0.0.jar``` to start your web server (on Linux systems, replace the
"\\" with a "/").

The `Endpoints.java` class contains the implementation of two endpoints. One that makes use of thymeleaf to render
an html page, and one that executes a remote call and responds with json.

Open http://localhost:8080/index to see the rendered html page.
If you add the URL parameter ```name=Samuel``` you will see a personalized greeting:

http://localhost:8080/index?name=Samuel

At http://localhost:8080/api you can see the json endpoint in action.
