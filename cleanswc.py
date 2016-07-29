#!python3

from rivuletpy.utils.backtrack import cleanswc
from rivuletpy.utils.io import loadswc, saveswc
import argparse

parser = argparse.ArgumentParser(description='Arguments for see anisotropic filters.')
parser.add_argument('--file', type=str, default=None, help='The file to filter')

parser.add_argument('--radius', dest='radius', action='store_true')
parser.add_argument('--no-radius', dest='radius', action='store_false')
parser.set_defaults(radius=True)

args = parser.parse_args()

swc = loadswc(args.file)
cleanedswc = cleanswc(swc, args.radius)
saveswc(args.file + '.cleaned.swc', cleanedswc)
