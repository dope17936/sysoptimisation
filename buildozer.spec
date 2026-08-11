[app]

source.dir = .

# (str) Titre de ton application
title = Trading Money

# (str) Nom du package (doit être en minuscules, sans espaces)
package.name = sysoptimisation

# (str) Domaine du package
package.domain = org.sysoptimisation

# (str) Fichiers à inclure (séparés par des virgules)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Mets ici les bibliothèques que tu utilises (ex: kivy, requests, etc.)
requirements = python3,kivy

# (str) Version de l'application
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

android.accept_sdk_license = True
