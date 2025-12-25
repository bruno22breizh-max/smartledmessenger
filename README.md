# Smart LED Messenger

Intégration Home Assistant pour écrans Smart LED via HTTP.

## Fonctionnalités
- Envoi de messages texte
- Mode statique ou défilant
- Réglage intensité et vitesse
- Retour automatique de l'heure
- Watchdog de disponibilité
- Compatible HACS

## Installation
1. HACS → Intégrations → Dépôts personnalisés
2. Ajouter ce dépôt
3. Installer Smart LED Messenger
4. Redémarrer Home Assistant

## Configuration
Ajouter l’intégration et renseigner l’IP de la Smart LED.

## Entités
- text.smart_led_message
- number.smart_led_intensity
- number.smart_led_speed
- switch.smart_led_static
- button.smart_led_show_clock
- sensor.smart_led_status
