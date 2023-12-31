from ctm import Ctm
from bizhawk_movie import BizhawkMovie
from bizhawk_to_ctm import writeCtmFromBizhawkMovie
from typing import TextIO
import yaml
import argparse


def dumpCTMHeaderToYAML(ctmHeader: Ctm.Header, outFile: TextIO):
    headerMap: dict = {}
    headerMap["title_id"] = ctmHeader.title_id
    headerMap["version"] = ctmHeader.version
    headerMap["clock_init_time"] = ctmHeader.clock_init_time
    headerMap["movie_id"] = ctmHeader.movie_id
    headerMap["author"] = ctmHeader.author
    headerMap["rerecords"] = ctmHeader.rerecords
    yaml.dump(headerMap, outFile)


argparser = argparse.ArgumentParser(description="Convert Bizhawk 3DS movie files to ctm format")
subparsers = argparser.add_subparsers(dest='subparser_option')

make_config_parser = subparsers.add_parser('make_config', help='Generate a config from a ctm file')
make_config_parser.add_argument('-i', help='The ctm file to create a config from', metavar='IN_CTM', required=True)
make_config_parser.add_argument('-o', help='The output config file', metavar='OUT_CONFIG', default='config.yml')

convert_bz_to_ctm_parser = subparsers.add_parser('convert', help='Convert a Bizhawk 3DS movie file to ctm format')
convert_bz_to_ctm_parser.add_argument('-i', help='The bizhawk movie file to convert', metavar='IN_MOVIE_FILE', required=True)
convert_bz_to_ctm_parser.add_argument('-o', help='The output ctm file', metavar='OUT_CTM', default='out.ctm')
convert_bz_to_ctm_parser.add_argument('-c', help='The config file', metavar='CONFIG', default='config.yml')

args = argparser.parse_args()

if args.subparser_option == 'make_config':
    ctm = Ctm.from_file(args.i)
    with open(args.o, 'w') as outConfigFile:
        dumpCTMHeaderToYAML(ctm.header, outConfigFile)
    
if args.subparser_option == 'convert':
    bizhawkMovie = BizhawkMovie()
    with open(args.i, 'r') as inMovieFile:
        bizhawkMovie.readFromFile(inMovieFile)
        
    with open(args.o, 'wb') as outCTM:
        with open(args.c, 'r') as configFile:
            writeCtmFromBizhawkMovie(bizhawkMovie, configFile, outCTM)
