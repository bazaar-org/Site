Update on what happened across the GNOME project in the week from June 13 to June 20.

## Third Party Projects

**[Sjoerd Stendahl](https://matrix.to/#@sjoerdb93:matrix.org) says**

> This week I released Lockpicker.
> 
> Lockpicker is a tool to recover passwords from a hash. Essentially it functions as a front-end for hashcat, making it possible to do password recovery without the hassle of hashcat syntax in a GNOME native graphical interface.  It’s mainly useful for anyone that is curious about password recovery, security or as a companion app for CTF-challenges.
> 
> You can check it out on [Flathub](https://flathub.org/en/apps/se.sjoerd.lockpicker).
>
> ![](https://thisweek.gnome.org/_astro/Lockpicker.T76OApkd_Z1IBAxP.webp)

**[Luiggi R. Cardoso](https://matrix.to/#@luiggic:unredacted.org) reports**

> Draft's v2.3 is out now! 
> 
> Now Draft has a new backend and cleaner code, making it easier and faster to add features.
> 
> This new version brings:
> - Markdown-inspired styling to make it simpler to organize your notes and snippets;
> - Zoom functionality to make the text larger and easier to read;
> - Now the app fully follows your accent color, making the interface seamless with your desktop.
> 
> [Download it on Flathub](https://flathub.org/en/apps/io.gitlab.luiggircardoso.Draft) | [Contribute on GitLab](https://gitlab.com/luiggircardoso/Draft) | Weblate will be back soon!
>
> ![](https://thisweek.gnome.org/_astro/draft-screenshot.DbwfSS7g_2h2lcq.webp)

**[JumpLink](https://matrix.to/#@JumpLink:matrix.org) reports**

> [Learn 6502 Assembly](https://flathub.org/apps/eu.jumplink.Learn6502) (learn assembly programming on a virtual retro console) just shipped **0.7.0**. The app now speaks Hebrew, fully translated by Menachem (@naattxx), who also tested and contributed the new right-to-left support. That makes Hebrew our first RTL language and prepares the app for more. This release also welcomes a new Indonesian translation by Arif Budiman, alongside the usual round of small fixes and improvements.
>
> ![](https://thisweek.gnome.org/_astro/learn6502_v0.7.0_he.BOp9ZW7s_2kT4Jx.webp)

**[tanay](https://matrix.to/#@tanaybhomia:matrix.org) says**

> Whisp has surpassed 1,000 downloads this week within 15 days(I am in Awe, Thank you so so much). The application now includes several quality-of-life improvements, including the List module, tree-style lists for better organization, note pinning, and keyboard shortcuts for faster navigation.
> 
> Development is now moving into Phase 2, focused on expanding Whisp beyond note-taking. Planned features include a built-in Math Engine for calculations, unit and measurement conversions, and Image-to-Text functionality powered by OCR.
> 
> Thank you to everyone who has tried, reported issues, and contributed feedback. Community support has been invaluable in helping shape the project.
> 
> Project website: https://tanaybhomia.github.io/Whisp/
> Source code: https://github.com/tanaybhomia/Whisp
> 
> If you'd like to support development, UPI donations are now available through the website, and COFI support is planned soon.
>
> ![](https://thisweek.gnome.org/_astro/whisp.D7DFX3fS_xcLDA.webp)
>
> ![](https://thisweek.gnome.org/_astro/whisp2.BxwUibRK_Z1tEKmA.webp)

### Gitte [↗](https://codeberg.org/ckruse/Gitte)

A simple Git GUI for GNOME

**[Christian](https://matrix.to/#@christian:kruse.cool) reports**

> Gitte, a simple Git client for GNOME built with GTK4, libadwaita and Relm4, just got its 0.7.0 release! 🎉
> 
> The headline feature this time is a visual commit graph in the commit log: branches are drawn with color-coded lines, so commits off the mainline get a distinct per-branch color and it's much easier to follow how history actually branches and merges. Stashes and pending changes show up as commits in that graph too, giving you a complete picture of your repository at a glance. You can also drop multiple commits at once now.
> 
> Diffs got a lot smarter as well. Gitte now detects renames, and the word-based diff has been overhauled to highlight intra-line changes more often. There's also a new shortcut (`Ctrl+D`) to switch between staged and unstaged in the working copy view.
> 
> There's more control over your lists and directories: you can toggle whether Gitte recurses into untracked directories, and the branch and tag lists now have a configurable sort order, with global defaults available in the preferences.
> 
> This release also comes with a broad UI overhaul. The main layout has been greatly reworked (special thanks to Brage Fuglseth!), and the preferences dialog is now a standard Adwaita preferences dialog. The columns now each have a distinct background color, the sidebar was reorganized, and the commit-graph and "rebase in progress" banners were revamped. On top of that come nice new action buttons in the sidebar, better spinners if an operations takes a bit longer, pane widths kept in sync across all views, and the usual round of consistent title casing and spacing fixes.
> 
> Under the hood there's a performance pass too: file diff lists now show at most 100 files (30 expanded by default, with an option to force loading everything), more operations run asynchronously, and the diff view isn't reloaded when it doesn't need to be.
> 
> And of course there's the usual pile of fixes: diff lines are redrawn on theme switch, scroll position is preserved while staging and unstaging, long labels break correctly, tag badges got a better color, and the window size is now saved correctly — including when quitting with `Ctrl+Q`.
> 
> Get it on [Flathub](https://flathub.org/apps/de.wwwtech.gitte), [for macOS](hhttps://gitlab.com/dehesselle/gitte_macos/-/releases/v0.7.0+36) or [have a look at the Code](https://codeberg.org/ckruse/Gitte).
>
> ![](https://thisweek.gnome.org/_astro/gitte-commit-graph.striOZ-l_Z24BgUw.webp)
>
> ![](https://thisweek.gnome.org/_astro/gitte-working-copy-view.BDrVL5Fq_Z1UuMH8.webp)

### GDM Settings [↗](https://gdm-settings.github.io)

Customize your login screen.

**[Mazhar Hussain](https://matrix.to/#@realmazharhussain:matrix.org) says**

> It has been almost 2 years since I last posted about GDM Settings on TWIG. While there have been some releases during that time, the development wasn't happening really consistently. I'm really sad to announce that the development of GDM Settings is on hold for now. I'm not sure when (or if) I'll pick up the development of this app again.
> 
> See [issue#324](https://github.com/gdm-settings/gdm-settings/issues/324) for information.
> 
> Thank you all for the support! It really meant a lot. ❤️

## Shell Extensions

**[Christian W](https://matrix.to/#@cwittenberg:matrix.org) reports**

> macOS-style text capture now also for GNOME: select any screen area, OCR it, copy instantly, optionally translate with this new extension https://extensions.gnome.org/extension/10209/snap-text-extractor/
>
> ![](https://thisweek.gnome.org/_astro/snap_text.B2deEQXo_Z1mgval.webp)

**[Tomáš Gažovič](https://matrix.to/#@todevelopers:matrix.org) says**

> RSS Feed extension is back after a long time and ported to latest GNOME. Same old feeds, but with a modern look. If you like your news directly from shell you can give it a try https://extensions.gnome.org/extension/948/rss-feed
> Project page: https://github.com/todevelopers/gnome-shell-extension-rss-feed

## Miscellaneous

**[balooii](https://matrix.to/#@balooii_:matrix.org) reports**

> For the two people out there that might be interested in trying out GIMP 0.54 from 1996 on your modern Linux system: Now you can, I created a Flatpak just for fun. It's the last version using Motif before it's creators decided to kick off a little toolkit called GTK... https://gitlab.gnome.org/balooii/gimp-0.54
>
> ![](https://thisweek.gnome.org/_astro/gimp.BbFPZO4u_ZlMkAt.webp)

### GNOME OS [↗](https://os.gnome.org)

The GNOME operating system, development and testing platform

**[Bilal Elmoussaoui](https://matrix.to/#@bilelmoussaoui:gnome.org) reports**

> GNOME OS is now using oo7 by default as a replacement of gnome-keyring-daemon, oo7-portal for the XDG Secrets portal implementation and oo7-cli as a replacement for secret-tool.

# That’s all for this week!

See you next week, and be sure to stop by [#thisweek:gnome.org](https://matrix.to/#/#thisweek:gnome.org) with updates on your own projects!
