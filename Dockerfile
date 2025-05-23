FROM odoo:18.0

# Set environment variables
ENV HOST=0.0.0.0 \
    PORT=8069

# Optional: Copy your custom modules
COPY ./custom_addons /mnt/extra-addons

# Make sure permissions are correct
RUN chown -R odoo:odoo /mnt/extra-addons

# Optional: Install extra dependencies
# RUN pip3 install -r requirements.txt

# Expose the Odoo port
EXPOSE 8069

CMD ["odoo"]
