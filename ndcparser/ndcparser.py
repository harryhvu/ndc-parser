
def format_product_ndc(product_ndc):
    product_ndc = str(product_ndc).strip()
    if '-' in product_ndc:
        ndc_split = product_ndc.split('-')
        formatted_ndc = f'{ndc_split[0].zfill(5)}{ndc_split[1].zfill(4)}'
        return formatted_ndc
    else:
        formatted_ndc = product_ndc.zfill(9)
        return formatted_ndc


def format_ndc(ndc):
    ndc = str(ndc).strip()
    if len(ndc.split('-')) == 3:
        ndc_split = ndc.split('-')
        formatted_ndc = f'{ndc_split[0].zfill(5)}{ndc_split[1].zfill(4)}{ndc_split[2].zfill(2)}'
        return formatted_ndc
    elif ndc.isnumeric():
        formatted_ndc = ndc.zfill(11)
        return formatted_ndc


def _parse_ndc(ndc):
    ndc = str(ndc).strip()
    formatted_ndc = format_ndc(ndc)
    labeler_code = formatted_ndc[0:5]
    product_code = formatted_ndc[5:9]
    package_code = formatted_ndc[9:11]
    return (labeler_code, product_code, package_code)


class _Ndc:
    def __init__(self, labeler, product, package, ndc11, ndc11_delimited, ndc9, ndc9_delimited):
        self.labeler = labeler
        self.product = product
        self.package = package
        self.ndc11 = ndc11
        self.ndc11_delimited = ndc11_delimited
        self.ndc9 = ndc9
        self.ndc9_delimited = ndc9_delimited


class NdcParser:
    def parse(ndc):
        parsed_ndc = _parse_ndc(ndc)
        labeler = parsed_ndc[0]
        product = parsed_ndc[1]
        package = parsed_ndc[2]
        ndc11 = f'{parsed_ndc[0]}{parsed_ndc[1]}{parsed_ndc[2]}'
        ndc11_delimited = f'{parsed_ndc[0]}-{parsed_ndc[1]}-{parsed_ndc[2]}'
        ndc9 = f'{parsed_ndc[0]}{parsed_ndc[1]}'
        ndc9_delimited = f'{parsed_ndc[0]}-{parsed_ndc[1]}'
        ndc_obj = _Ndc(labeler=labeler, product=product, package=package, ndc11=ndc11, ndc11_delimited=ndc11_delimited, ndc9=ndc9, ndc9_delimited=ndc9_delimited)
        return ndc_obj
