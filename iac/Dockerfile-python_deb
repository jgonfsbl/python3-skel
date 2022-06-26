# ##################################### #
#                                       #
#   How-To build this container image   #
#                                       #
# ##################################### #
#
#
# Local build
# -----------
# docker build \
#   -f iac/Dockerfile-python_deb \
#   --build-arg VERSION=`cat src/VERSION` \
#   --build-arg GIT_BRANCH=`git branch --show-current` \
#   -t ea1het/my_test_container:`cat src/VERSION` .
#
#
# Platform specific images (when you build for your own platform)
# ---------------------------------------------------------------
# docker build \
#   --build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
#   --build-arg VERSION=`cat src/VERSION` \
#   --build-arg GIT_BRANCH=`git branch --show-current` \
#   -t registry.gitlab.com/ea1het/my_test_container:`cat src/VERSION` .
#
#
# Cross-compile platform independent images (when you use a build facility
# in your platform to cross-compile for another platform)
# ------------------------------------------------------------------------
# docker buildx ls
# docker buildx create --name testbuilder
# docker buildx use testbuilder
# docker buildx inspect --bootstrap
# docker buildx build \
#   --platform linux/arm/v6 \
#   --build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
#   --build-arg VERSION=`cat src/VERSION` \
#   --build-arg GIT_BRANCH=`git branch --show-current` \
#   -t registry.gitlab.com/ea1het/my_test_container:`cat src/VERSION` --push .
#
# #############################################################################

FROM python:3.10.4-slim-bullseye AS build-image
LABEL maintainer="Jonathan Gonzalez <j@0x30.io>"
ENV PYTHONUNBUFFERED 1
ARG GIT_BRANCH

# - Create and activate virtual environment using final folder name to avoid path issues with packages
WORKDIR /app/
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# - Install project requirements
COPY ./requirements/ ./requirements/
COPY ./requirements/$GIT_BRANCH.txt ./requirements.txt
RUN pip3 install --no-cache-dir wheel && pip3 install --no-cache-dir -r requirements.txt


FROM python:3.10.4-slim-bullseye AS runner
LABEL maintainer="Jonathan Gonzalez <j@0x30.io>"
ENV PYTHONUNBUFFERED=1

# - Switch to program folder and load previous docker layer
WORKDIR /app/
COPY --from=build-image /opt/venv /opt/venv

# Enable Virtualenv and run the program
ENV PATH="/opt/venv/bin:$PATH"
COPY ./src/ .
COPY ./events/ ./events/
WORKDIR /app/src
CMD ["python3", "app.py" ]
