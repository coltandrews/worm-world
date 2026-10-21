# Worm World

Turn-based, third-person worm warfare in the browser. Up to four laptops online, or hotseat on one.

- **Play:** open the site, type your name, then **Host online** and share the 4-letter code (or the invite link). Friends hit **Join**, then **Ready up**; the host starts once everyone is ready.
- **Controls:** WASD crawl (Shift hurry), Space jump, mouse aim, click to fire (hold to charge), Tab weapon wheel, B shop, Enter chat, M mute.

## How it works

- `index.html` is the whole game (three.js r128 from cdnjs).
- Networking is peer-to-peer WebRTC via [Trystero](https://github.com/dmotz/trystero) (Nostr relays for signaling). The host's browser runs the simulation; other players send inputs and receive snapshots plus effect events (craters are replayed locally, so terrain stays identical).
- `api/ice.js` is a Vercel function that hands out ICE servers. Set `TURN_KEY_ID` and `TURN_KEY_API_TOKEN` (Cloudflare Calls TURN) in the Vercel project if players are on networks that block direct connections; without them it uses public STUN, which works on most home networks.

## Deploy

Static site + one serverless function. Import the repo in Vercel with no build settings, or run `vercel --prod` from this folder.
