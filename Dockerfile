FROM odoo:18.0

ENV HOST=0.0.0.0 \
    PORT=8069 \
    ADDONS_PATH=/mnt/extra-addons

USER root
RUN mkdir -p /mnt/extra-addons
COPY ./custom_addons /mnt/extra-addons
RUN chown -R odoo:odoo /mnt/extra-addons

EXPOSE 8069

USER odoo

CMD ["odoo"]
