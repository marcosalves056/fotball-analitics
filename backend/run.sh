#!/bin/bash
echo "Iniciando servidor ASGI (Django + WebSocket)..."
daphne -b 0.0.0.0 -p 8000 app.asgi:application
