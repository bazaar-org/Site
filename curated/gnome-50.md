**March 18, 2026**

The GNOME project is delighted to unveil **GNOME 50**, a milestone that reflects six months of collective effort from our vibrant community. A heartfelt thank you goes to everyone who helped shape this release.

This new GNOME version is named “Tokyo”, to recognize the work done by the local organizers of GNOME.Asia Summit 2025. Thank you to everyone who helped with this amazing event!

## Parental Controls

GNOME's parental controls have made a massive leap forward in GNOME 50. For the first time it is now possible for parents and guardians to monitor screen time and set limits for child accounts, including bedtime schedules. The new features allow automatically locking the screen when a screen limit or bedtime is reached. Parents and guardians also have the ability to extend screen time past the limit when needed.

![Parental Controls App Screenshot](https://release.gnome.org/50/parental-app-screenshot.webp)

Parental Controls are integrated in multiple places, including the Settings app, which links to the Parental Controls app. GNOME's Parental Controls app has also been completely updated, with a fresh modern look.

Under the hood, the foundations for web filtering support has also been added — a backend service that can enforce content filters for child accounts once the user interface is completed in future updates, allowing age‑appropriate web restrictions without breaking web security or relying on curated lists.

Thank you to [Endless](https://endlessglobal.com/foundation-grants) for funding this important work to make GNOME more accessible to young people and their carers!

## Accessibility Enhancements

GNOME 50 includes several exciting new developments for assistive technology users. First, the **Orca** screen reader has received a range of significant improvements:

* A **brand new preferences window** has an enhanced design and is more consistent with other GNOME apps.
* All **settings are now global**, eliminating the need to save settings on a per-application basis, such as for web browsers. Settings can, of course, still be saved on a per-application basis when doing so is desired.
* **Automatic language switching** has been added both for web content and app UI.
* **Browse mode** has been extended to all document content, and **sticky mode** has been adjust to automatically turn on for Electron apps. **Braille support** has also been enhanced.
* **Mouse Review** can now be used in Wayland sessions.

Second, an exciting new development in GNOME 50 is the introduction of a new **Reduced Motion** option. This can be enabled in the Seeing section of the Accessibility settings, and adjusts interface animations so as to reduce any discomfort or distraction that they may cause.

![Reduced Motion in Settings](https://release.gnome.org/50/reduced-screenshot.webp)

## Document Annotation

GNOME's **Document Viewer** app has had a limited annotation feature for years. For GNOME 50, this feature has been overhauled, expanded, and brought into the modern age. Adding annotations to documents can now be easily done with the click of a button from the main view. The feature allows not just adding annotations as text, but also adding lines and highlights. It has a simple yet powerful interface, with a choice of colors and line thicknesses, and an eraser in case you make a mistake. Altogether this is a fantastic feature that we are sure people will find useful.

![Annotations Feature in Document Viewer](https://release.gnome.org/50/document-viewer-annotations.webp)

## Files Improvements

GNOME's **Files** app has undergone extensive improvements for version 50, focusing on performance, reliability, and a more refined user interface.

### Performance and stability improvements

* Snappier experience thanks to **faster thumbnail and icon loading**.
* A general **reduction in memory usage** across the application.
* Greatly **increased test coverage**, to help keep the bug count low
* Technical modernization with increasing use of the **Blueprint** markup language for UI definitions, as well as and making use of the **Glycin** library for high-performance, sandboxed image decoding.

### Interface enhancements

* The **batch Rename** feature has been reworked to be more intuitive, and now features visual highlights for replaced text.
* File properties have transitioned to **"pop-out" free-floating windows**.
* A new **dialog for managing captions** has been added for the grid view.
* File operation descriptions in the sidebar have been shortened to keep the interface clean and readable.

### Behavior improvements

* When searching, **multiple filters** can now be used when filtering by file type.
* The pathbar has been updated to support **case-insensitive completions**.


## Calendar Updates

**Calendar** has received a significant set of productivity and navigation improvements for GNOME 50. A major highlight is the new **attendee list**, which allows you to see who is invited to an event, including whether their attendance is required or optional. This is a foundational step toward full invitation management in future versions.

The experience of managing events is also much smoother:
* **Redesigned Quick Add:** The popover for adding new events has been redesigned to be more intuitive and efficient.
* **ICS Export:** Previously, you could share individual events. Now you can also export your entire schedule at once.
* **Month View Refinements:** The Month view is more polished than ever, featuring a more prominent month name, improved event alignment, and smoother scrolling animations.
* **Regional Customization:** Calendar now respects the system setting for the first day of the week, ensuring your view matches your local preference.

Navigation and accessibility have also taken a leap forward. It is now possible to **navigate through events using the arrow keys** in the Month view, and the app now supports dedicated "Back" and "Forward" hardware buttons on mice and keyboards. Additionally, the month-switching logic has been refined to "clamp" to the beginning of the month, providing a more predictable experience when browsing through a long timeline.


![](appstream://org.gnome.Papers,appstream://org.gnome.Calendar)

## Settings Changes

Settings has received a number of welcome improvements for GNOME 50:

* **Date & Time** includes a new “first day of week” option, which is also respected by apps such as GNOME Calendar and Evolution, ensuring a consistent weekly view across the desktop.
* **Sound** now clearly distinguishes between input and output in the volume levels section, making it easier to understand what’s being controlled.
* **Modem Details** has updated details dialogs, which now use modern libadwaita widgets and layout conventions, improving visual consistency and aligning it with the rest of the Settings interface.
* **Color Management** has received a round of bug fixes, particularly around display calibration.

![Sound Mix in Settings](https://release.gnome.org/50/settings-sound-screenshot.webp)

## Remote Desktop

GNOME's built-in remote desktop capabilities have seen significant improvements in version 50. A major performance boost comes from new **hardware acceleration** support (using Vulkan and VA-API). By using your computer's graphics processor to stream video, remote sessions are now significantly smoother with much less lag and lower power consumption. Compatibility has also been improved for a wider range of hardware with the integration of **explicit sync**, which provides a more stable experience for those using NVIDIA drivers.

The remote desktop experience is also more seamless across different devices. New **HiDPI support** means that remote desktop clients can automatically scale the display to match the resolution of the screen being used. Furthermore, users can now utilize **camera redirection**, allowing them to use their local webcam from within a remote session, just like if it were plugged into the remote computer.

For system administrators and power users, authentication and session management have been bolstered. First, **Kerberos Authentication** support has been added, providing professional-grade security when using screen sharing or single user headless servers. Second, remote login now supports sessions started via the `gnome-headless-session` systemd service. These sessions are now much more reliable and will stay running even if the remote desktop system service needs to be restarted.

## Display Handling Improvements

GNOME's display technologies have received a massive set of stability and performance updates in GNOME 50.

* **Improved Variable Refresh Rate (VRR) and Fractional Scaling Support:** VRR and fractional scaling have both been improved for GNOME 50, with bug fixes, stability, and user experience improvements. Some distributions enabled these features in previous releases, so many users will have used them already. However, for other distros, these features are now enabled by default in GNOME 50.
  * For users with compatible monitors, **VRR** provides a tear-free experience where the display’s refresh rate matches the application's frame rate, resulting in significantly smoother motion.
  * **Fractional scaling** allows what is displayed on screen to be scaled in increments, to better suit a range of display densities. When it is enabled, users can natively select scales like 125% or 150% in the display settings. 
* **Low-Latency Cursor in VRR:** The mouse cursor now operates independently of the application's frame rate while VRR is active. This ensures the cursor remains fluid and responsive at the monitor’s maximum refresh rate (e.g., **144Hz**) even if a game or professional app is running at a lower frame rate.
* **NVIDIA Performance Boosts:** Workarounds for NVIDIA driver quirks have been implemented, targeting stuttering and frame-timing issues. The result is noticeably smoother window animations and general desktop fluidity for users with NVIDIA GPUs.
* **Next-Gen Color Management:** Support for version 2 of the Wayland color management protocol has landed. This provides the technical foundation for creative professionals to achieve higher color accuracy across different apps and hardware.

* **HDR Screen Sharing:** Building on GNOME's modern color pipeline, it's now possible to screen share monitors displaying High Dynamic range (HDR) content. This allows screen recording software to record the screen content with the same vivid colors as displayed on the physical screen.

## GNOME Circle

[Circle](https://circle.gnome.org) is GNOME's initiative to recognize and support the best community-created apps which use the GNOME platform. Since the last release, several new projects have joined the Circle, including:

* **[Gradia](https://flathub.org/apps/be.alexandervanhee.gradia):** An app for refining and annotating screenshots before you share them. It provides a professional touch to raw captures, allowing you to add elegant gradient backgrounds, drop shadows, and custom padding.

    ![Gradia screenshot](https://release.gnome.org/50/gradia-screenshot.webp)

    Whether you are preparing a quick visual for a colleague or high-quality assets for documentation, Gradia offers ten different annotation modes, including arrows, text, and censorship tools to clearly communicate your message. It also features a specialized mode to convert code snippets into clean, high-resolution images.

    ![Sudoku screenshot](https://release.gnome.org/50/sudoku-screenshot.webp)

* **[Sudoku](https://flathub.org/apps/io.github.sepehr_rs.Sudoku):** A modern puzzle app for solving classic number-placement challenges. It features a clean, distraction-free interface that scales perfectly across different screen sizes.

	Whether you are a beginner or an expert, the app includes helpful features like conflict highlighting and active-cell focus to help you stay engaged. It also supports full keyboard navigation and seamless game saving, so you can pick up your progress whenever you have a spare moment.

* **[Constrict](https://flathub.org/apps/io.github.wartybix.Constrict):** A video compression app designed to help you meet specific file size limits without the guesswork. Instead of manually experimenting with bitrates, you can simply set your target size, and the app automatically calculates the optimal settings for resolution, framerate, and audio quality.

    ![Constrict screenshot](https://release.gnome.org/50/constrict-screenshot.webp)

    Constrict performs all processing locally and supports a variety of modern codecs, including H.264, HEVC, AV1, and VP9. It also features a bulk compression mode for processing multiple videos at once and allows you to set framerate limits to balance smoothness with visual clarity.

* **[Sessions](https://flathub.org/apps/com.pojtinger.felicitas.Sessions)** A simple visual timer app designed specifically for the pomodoro technique, helping you stay productive by breaking work into focused sessions with regular breaks.

    ![Sessions screenshot](https://release.gnome.org/50/session-screenshot.webp)

![Apps](appstream://be.alexandervanhee.gradia,appstream://io.github.sepehr_rs.Sudoku,appstream://io.github.wartybix.Constrict,appstream://com.pojtinger.felicitas.Sessions)

## Thanks for Your Support ❤️

This release wouldn’t have been possible without the amazing contributions, feedback, and encouragement from our community. If you’d like to help us continue improving, please consider supporting the project financially. Every donation helps us dedicate more time and resources to building something better for everyone.
