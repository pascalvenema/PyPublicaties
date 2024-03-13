import xml.etree.ElementTree as ET

class OfficielePublicatie:
    def __init__(self):
        self.identifier = []
        self.title = []
        self.type = []
        self.language = []
        self.authority = []
        self.creator = []
        self.modified = []
        self.temporal = []
        self.spatial = []
        self.alternative = []
        self.date = []
        self.hasVersion = []
        self.source = []
        self.requires = []
        self.isPartOf = []
        self.isrequiredby = []
        self.isreplacedby = []
        self.hasPart = []
        self.subject = []
        self.available = []
        self.abstract = []
        self.publisher = []
        self.issued = []
        self.replaces = []
        self.aanhangsel = []
        self.aanhangselnummer = []
        self.adviesRvs = []
        self.bedrijfsnaam = []
        self.behandeldDossier = []
        self.betreft = []
        self.betreftopschrift = []
        self.betreftRegeling = []
        self.bijlage = []
        self.datumBrief = []
        self.datumIndiening = []
        self.datumOndertekening = []
        self.datumOntvangst = []
        self.datumTotstandkoming = []
        self.datumVergadering = []
        self.deurwaardersdossier = []
        self.documentstatus = []
        self.documenttitel = []
        self.dossiernummer = []
        self.dossiertitel = []
        self.effectgebied = []
        self.einddatum = []
        self.datumEindeReactietermijn = []
        self.eindpagina = []
        self.externeBijlage = []
        self.gebiedsmarkering = []
        self.gemeentenaam = []
        self.geometrie = []
        self.geometrie = []
        self.geometrielabel = []
        self.hectometernummer = []
        self.heeftMededeling = []
        self.hoofddocument = []
        self.huisnummer = []
        self.huisletter = []
        self.huisnummertoevoeging = []
        self.indiener = []
        self.handelingenitemnummer = []
        self.jaargang = []
        self.kadastraleSectie = []
        self.ketenid = []
        self.ligtInGemeente = []
        self.ligtInProvincie = []
        self.materieelUitgewerkt = []
        self.mededelingOver = []
        self.ondernummer = []
        self.ontvanger = []
        self.organisatietype = []
        self.perceelnummer = []
        self.persoonsgegevens = []
        self.plaatsTotstandkoming = []
        self.postcode = []
        self.postcodeHuisnummer = []
        self.provincie = []
        self.provincienaam = []
        self.publicatienummer = []
        self.publicatienaam = []
        self.besluitReferendabiliteit = []
        self.referentienummer = []
        self.rijkswetnummer = []
        self.bekendmakingBetreffendePlan = []
        self.startdatum = []
        self.startpagina = []
        self.straatnaam = []
        self.subrubriek = []
        self.sysyear = []
        self.sysnumber = []
        self.sysseqnumber = []
        self.terinzageleggingBG = []
        self.terinzageleggingOP = []
        self.typeVerkeersbesluit = []
        self.verdragnummer = []
        self.vereisteVanBesluit = []
        self.vergaderjaar = []
        self.verkeersbordcode = []
        self.versieinformatie = []
        self.versienummer = []
        self.vraagnummer = []
        self.waterschapsnaam = []
        self.wegcategorie = []
        self.weggebruiker = []
        self.wegnummer = []
        self.woonplaats = []
        self.zittingsdatum = []
        self.product_area = []
        self.content_area = []
        self.datumTijdstipWijzigingWork = []
        self.datumTijdstipWijzigingExpression = []
        self.url = []
        self.prefferedUrl = []
        self.itemUrl = []
        self.timestamp = []
        
    @classmethod
    def from_xml_element(cls, element: ET.Element, namespaces: dict) -> 'OfficielePublicatie':
        op = cls()
        for child in element.findall('.//*', namespaces):
            tag = cls.parse_namespaced_tag(child.tag)

            if tag not in op.__dict__:
                continue

            if child.attrib:
                value_dict = child.attrib
                value_dict['value'] = child.text.strip() if child.text else ""
                op.__dict__[tag].append(value_dict)
            else:
                op.__dict__[tag].append(child.text.strip() if child.text else "")

        return op

    @staticmethod
    def parse_namespaced_tag(tag: str) -> str:
        return tag.split('}', 1)[-1] if '}' in tag else tag

    def __iter__(self):
        for key in self.__dict__:
            yield {key: getattr(self, key)}

    def __repr__(self):
        return f"<OfficielePublicatie identifier={self.identifier}, title={self.title}>"