ARG KEA_REPO=public/isc/kea-dev
ARG KEA_VERSION=2.7.7-isc20250326114722
# Indicate if the premium packages should be installed.
# Valid values: "premium" or empty.
ARG KEA_PREMIUM=""


FROM debian:12.9-slim AS debian-base

# Container with a modern Supervisord installled.
FROM debian-base AS supervisor-base
RUN apt-get update \
        && apt-get install \
        -y \
        --no-install-recommends \
        python3.11=3.11.* \
        python3-pip=23.* \
        python3-setuptools=66.* \
        supervisor \
        wget \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir -p /var/log/supervisor

# Server containers
FROM supervisor-base AS server
ENTRYPOINT [ "/bin/sh", "-c", \
        "supervisord -c /etc/supervisor/supervisord.conf" ]
EXPOSE 8080
HEALTHCHECK CMD [ "supervisorctl", "status " ]

FROM supervisor-base AS kea-base
# Install Kea dependencies
RUN apt-get update \
        && apt-get install \
        -y \
        --no-install-recommends \
        curl=7.88.* \
        apt-transport-https=2.6.* \
        gnupg=2.2.* \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Install Kea from Cloudsmith
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
ARG KEA_REPO
ARG KEA_VERSION
RUN curl https://dl.cloudsmith.io/${KEA_REPO}/setup.deb.sh | bash \
        && apt-get update \
        && apt-get install \
        --no-install-recommends \
        -y \
        apt-utils \
        isc-kea-ctrl-agent=${KEA_VERSION} \
        isc-kea-dhcp4=${KEA_VERSION} \
        isc-kea-dhcp6=${KEA_VERSION} \
        isc-kea-admin=${KEA_VERSION} \
        isc-kea-common=${KEA_VERSION} \
        isc-kea-hooks=${KEA_VERSION} \
        isc-kea-mysql=${KEA_VERSION} \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir -p /var/run/kea/

# Install premium packages. The KEA_REPO variable must
# be set to the private repository and include an access token.
# Docker ignores this section if the KEA_PREMIUM is empty - thanks
# to this, the image builds correctly when the token is unknown.
FROM kea-base AS keapremium-base
ARG KEA_PREMIUM
ARG KEA_VERSION
# Execute only if the premium is enabled
RUN [ "${KEA_PREMIUM}" != "premium" ] || ( \
        apt-get update \
        && apt-get install \
        --no-install-recommends \
        -y \
        isc-kea-premium-cb-cmds=${KEA_VERSION} \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir -p /var/run/kea/ \
        && ldconfig \
        )

ENTRYPOINT [ "/bin/sh", "-c", \
        "supervisord -c /etc/supervisor/supervisord.conf" ]
EXPOSE 8080
HEALTHCHECK CMD [ "supervisorctl", "status " ]