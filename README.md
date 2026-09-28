# YouTube Music Desktop App COPR packaging

This repository repackages the official YouTube Music Desktop App RPMs for
Fedora COPR. It does not build the application from source. The spec downloads
the exact upstream release assets and verifies their SHA-256 checksums before
extracting their payloads.

## Update procedure

1. Obtain the current x86_64 and ARM64 RPM versions, download URLs, and
   SHA-256 digests from [YouTube Music Desktop App releases](https://github.com/ytmdesktop/ytmdesktop/releases).
2. Update `Version`, `Release`, the source URLs and checksums in
   `youtube-music-desktop-app.spec`, and `version` in `.copr/Makefile`.
3. Build from SCM in COPR for Fedora 43, 44, 45, and Rawhide.

Install the resulting package with:

```bash
sudo dnf copr enable ok8219/youtube-music-desktop-app
sudo dnf install youtube-music-desktop-app
```
