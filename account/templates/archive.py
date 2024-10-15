# <!-- templates/registration/login.html -->
# {% extends "master.html" %}
#
# {% block title %}
#     Login{% endblock %}
#
# {% load django_bootstrap5 %}
#
# {% block content %}
#
#     <h2>Log In</h2>
#     <form>
#         {% bootstrap_form form %}
#     </form>
#
#
# {% endblock %}
#
#
# <!-- templates/registration/login.html -->
# {% extends "master.html" %}
#
# {% block title %}
# Login{% endblock %}
#
#
# {% block content %}
#
#   <h2>Log In</h2>
#
#     <form method="post">
#         {% csrf_token %}
#         {{ form }}
#         <button type="submit">Log In</button>
#     </form>
#
# {% endblock %}
