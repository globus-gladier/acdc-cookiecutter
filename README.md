# ACDC Cookie Cutter Portal

This Cookie-Cutter project will get you started quickly with a new ACDC portal.

[ACDC](https://acdc.alcf.anl.gov/) (ALCF Community Data Co-Op) is a project comprised of many science portals to enable rich contextual access to science data. We don't currently have formal requirements for adding new portals to ACDC, simply ask Nick or Ryan and we'll get back to you.

This guide will prepare you for creating your own portal, structured so that we can deploy it for you at the ACDC site. The project structure is important for enabling us to do so. The basic process is creating your project skeleton using cookiecutter, running through the Django Globus Portal Framework guide for getting started, then getting back to us with your changes.

### Getting Started

First, clone Cookiecutter. We recommend at least python 3.10 or higher. This guide is similar to the
Django Globus Portal Framework [installation guide](https://django-globus-portal-framework.readthedocs.io/en/latest/), with some differences to deploy it on ACDC. Get started with cloning the project locally to your system:

```
python -m venv venv
source venv/bin/activate
pip install cookiecutter
cookiecutter https://github.com/globus-gladier/acdc-cookiecutter.git
```

Two important items need to be addressed before you can customize your portal:
* A Globus Search Index UUID
    * See the [DGPF Index Creation Guide](https://django-globus-portal-framework.readthedocs.io/en/latest/tutorial/search/index-creation.html) to create an index UUID.
* Globus App Credentials to enable login
    * See the [DGPF Globus App Guide](https://django-globus-portal-framework.readthedocs.io/en/latest/tutorial/installation-and-setup.html#globus-auth) to create your App Credentials
    * Login isn't strictly needed if your search data is public

The search index UUID can be set on your portal under project_name/app.py. 

#### Environment Setup

Run this to install and run your portal

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

You will get warnings for not setting up a search index, or if your App Credentials above are not setup.


Your basic portal should be setup by this point.

### Customizing Your Portal

Continue to follow the guide outlined starting a portal in the [Django Globus Portal Framework docs](https://django-globus-portal-framework.readthedocs.io/en/latest/tutorial/search/index-creation.html#index-creation-and-ingest). The cookiecutter will have already moved files into place for you, but you will still need to edit files to suit your project.

#### Templates

Follow the search ingest guide in the DGPF docs above. It's usually good to start with editing the detail-overview.html and search-results.html files to begin customizing your portal how you like it.

#### What is the "testing" folder?

ACDC has some project structure differences from a normal Django setup. Each "portal" is setup as a separate Django app and installed as one cohesive portal. As such, the "testing" folder is setup for local development but isn't used when deployed to ACDC. Only app files within your project's main directory will be used.

#### What dependencies can I install?

Please check with us if you need any custom dependencies. Simple ones are usually fine, but our deployment structure constrains what we can have individual portals define (We'll likely change how we deploy portals in the future to make this more flexible)

#### What custom styling can I use?

We prefer to keep with the ACDC styling. For basic portals, this will happen automatically. Let us know if you want the base static files if you are doing anything complex.

#### Can I define custom DB models?

Yes! Please let us know if you do, and please don't go too crazy with how much data you store in them. Storing data in Globus Search is always preferable if possible.