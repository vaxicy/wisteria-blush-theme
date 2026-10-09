// Wisteria Blush Theme — wisteria violet, dusty blush and peach
import { readFile } from 'node:fs/promises';

const FLOWER_PALETTE = {
  wisteria: '#E0BBE4',
  violet: '#957DAD',
  blush: '#D291BC',
  pink: '#FEC8D8',
  peach: '#FFDFD3',
};

export class WisteriaBlush {
  constructor(name = 'Morning sky') {
    this.name = name;
    this.colors = Object.values(FLOWER_PALETTE);
  }

  /** Blend two colors into a soft flower-inspired shade. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channels = a.map((value, i) => Math.round(value * (1 - ratio) + b[i] * ratio));
    return '#' + channels.map((value) => value.toString(16).padStart(2, '0')).join('');
  }

  async describe(file) {
    const content = await readFile(file, 'utf8');
    return { name: this.name, colors: this.colors, content };
  }
}

const cloud = new WisteriaBlush();
console.log(cloud.blend(FLOWER_PALETTE.wisteria, FLOWER_PALETTE.peach));
