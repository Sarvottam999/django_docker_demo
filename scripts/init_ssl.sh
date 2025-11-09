#!/bin/bash
set -e

DOMAIN1=birlallf.org
DOMAIN2=www.birlallf.org

echo "Stopping nginx..."
docker compose -f docker-compose.prod.yml stop nginx

echo "Requesting certificates for $DOMAIN1 and $DOMAIN2..."
sudo certbot certonly --standalone -d $DOMAIN1 -d $DOMAIN2 --non-interactive --agree-tos -m sarvottamsharmaa@email.com

echo "Starting nginx..."
docker compose -f docker-compose.prod.yml up -d nginx

echo "SSL setup complete!"
