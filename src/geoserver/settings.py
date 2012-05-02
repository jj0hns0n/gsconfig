from geoserver.support import atom_link, xml_property, write_string, write_bool, string_list, write_string_list, attribute_list, key_value_pairs, write_dict, ResourceInfo
import string

class _settings(object):
    def __init__(self, charset, numDecimals, verbose, verboseExceptions):
        self.charset = charset
        self.numDecimals = numDecimals
        self.verbose = verbose
        self.verboseExceptions = verboseExceptions

def _read_settings(node):
    charset = node.find("charset")
    numDecimals = node.find("numDecimals")
    verbose = node.find("verbose")
    verboseExceptions = node.find("verboseExceptions")

    if charset is not None:
        charset = charset.text
    if numDecimals is not None:
        numDecimals = numDecimals.text
    if verbose is not None:
        verbose = verbose.text
    if verboseExceptions is not None:
        verboseExceptions = verboseExceptions.text
    return _settings(charset, numDecimals, verbose, verboseExceptions)

def _write_settings(builder, settings):
    builder.start("settings", dict())
    if settings.charset is not None:
        builder.start("charset", dict())
        builder.data(settings.charset)
        builder.end("charset") 
    if settings.numDecimals is not None:
        builder.start("numDecimals", dict())
        builder.data(settings.numDecimals)
        builder.end("numDecimals") 
    if settings.verbose is not None:
        builder.start("verbose", dict())
        builder.data(settings.verbose)
        builder.end("verbose") 
    if settings.verboseExceptions is not None:
        builder.start("verboseExceptions", dict())
        builder.data(settings.verboseExceptions)
        builder.end("verboseExceptions") 
    builder.end("settings")

class _contact(object):
    def __init__(self, contactPerson, contactOrganization, contactPosition, addressType, address, addressCity, addressState, addressPostalCode, addressCountry, contactVoice, contactFacsimile, contactEmail):
        self.contactPerson = contactPerson
        self.contactOrganization = contactOrganization
        self.contactPosition = contactPosition
        self.addressType = addressType
        self.address = address
        self.addressCity = addressCity
        self.addressState = addressState
        self.addressPostalCode = addressPostalCode
        self.addressCountry = addressCountry
        self.contactVoice = contactVoice
        self.contactFacsimile = contactFacsimile
        self.contactEmail = contactEmail

def _read_contact(node):
    contactPerson = node.find("contactPerson")
    contactOrganization = node.find("contactOrganization")
    contactPosition = node.find("contactPosition")
    addressType = node.find("addressType")
    address = node.find("address")
    addressCity = node.find("addressCity")
    addressState = node.find("addressState")
    addressPostalCode = node.find("addressPostalCode")
    addressCountry = node.fine("addressCountry")
    contactVoice = node.fine("contactVoice")
    contactFacsimile = node.find("contactFacsimile")
    contactEmail = node.find("contactEmail")

    if contactPerson is not None:
        contactPerson = contactPerson.text
    if contactOrganization is not None:
        contactOrganization = contactOrganization.text
    if contactPosition is not None:
        contactPosition = contactPosition.text
    if addressType is not None:
        addressType = addressType.text
    if address is not None:
        address = address.text
    if addressCity is not None:
        addressCity = addressCity.text
    if addressState is not None:
        addressState = addressState.text
    if  addressPostalCode is not None:
        addressPostalCode = addressPostalCode.text
    if addressCountry is not None:
        addressCountry = addressCountry.text
    if contactVoice is not None:
        contactVoice = contactVoice.text
    if contactFacsimile is not None:
        contactFacsimile = contactFacsimile.text
    if contactEmail is not None:
        contactEmail = contactEmail.text
    return _contact(contactPerson, contactOrganization, contactPosition, addressType, address, addressCity, addressState, addressPostalCode, addressCountry, contactVoice, contactFacsimile, contactEmail)

def _write_contact(builder, contact):
    builder.start("contact", dict())
    if contact.contactPerson is not None:
        builder.start("contactPerson", dict())
        builder.data(contact.contactPerson)
        builder.end("contactPerson")
    if contact.contactOrganization is not None:
        builder.start("contactOrganization", dict())
        builder.data(contact.contactOrganization)
        builder.end("contactOrganization")
    if contact.contactPosition is not None:
        builder.start("contactPosition", dict())
        builder.data(contact.contactPosition)
        builder.end("contactPosition")
    if contact.addressType is not None:
        builder.start("addressType", dict())
        builder.data(contact.addressType)
        builder.end("addressType")
    if contact.address is not None:
        builder.start("address", dict())
        builder.data(contact.address)
        builder.end("address")
    if contact.addressCity is not None:
        builder.start("addressCity", dict())
        builder.data(contact.addressCity)
        builder.end("addressCity")
    if contact.addressState is not None:
        builder.start("addressState", dict())
        builder.data(contact.addressState)
        builder.end("addressState")
    if contact.addressPostalCode is not None:
        builder.start("addressPostalCode", dict())
        builder.data(contact.addressPostalCode)
        builder.end("addressPostalCode")
    if contact.addressCountry is not None:
        builder.start("addressCountry", dict())
        builder.data(contact.addressCountry)
        builder.end("addressCountr")
    if contact.contactVoice is not None:
        builder.start("contactVoice", dict())
        builder.data(contact.contactVoice)
        builder.end("contactVoice")
    if contact.contactFacsimile is not None:
        builder.start("contactFacsimile", dict())
        builder.data(contact.contactFacsimile)
        builder.end("contactFacsimile")
    if contact.contactEmail is not None:
        builder.start("contactEmail", dict())
        builder.data(contact.contactEmail)
        builder.end("contactEmail")
    builder.end("contact")


class _jai(object):
    def __init__(self, allowInterpolation, recycling, tilePriority, tileThreads, memoryCapacity, memoryThreshold, imageIOCache, pngAcceleration, jpegAcceleration, allowNativeMosaic):
        self.allowInterpolation = allowInterpolation
        self.recycling = recycling
        self.tilePriority = tilePriority
        self.tileThreads = tileThreads
        self.memoryCapacity = memoryCapacity
        self.memoryThreshold = memoryThreshold
        self.imageIOCache = imageIOCache
        self.pngAcceleration = pngAcceleration
        self.jpegAcceleration = jpegAcceleration
        self.allowNativeMosaic = allowNativeMosaic

def _read_jai(node):
    allowInterpolation = node.find("allowInterpolation")
    recycling = node.find("recycling")
    tilePriority = node.find("tilePriority")
    tileThreads = node.find("tileThreads")
    memoryCapacity = node.find("memoryCapacity")
    memoryThreshold = node.find("memoryThreshold")
    imageIOCache = node.find("imageIOCache")
    pngAcceleration = node.find("pngAcceleration")
    jpegAcceleration = node.find("jpegAcceleration")
    allowNativeMosaic = node.find("allowNativeMosaic")

    if allowInterpolation is not None:
        allowInterpolation = allowInterpolation.text
    if recycling is not None:
        recycling = recycling.text
    if tilePriority is not None:
        tilePriority = tilePriority.text
    if tileThreads is not None:
        tileThreads = tileThreads.text
    if memoryCapacity is not None:
        memoryCapacity = memoryCapacity.text
    if memoryThreshold is not None:
        memoryThreshold = memoryThreshold.text
    if imageIOCache is not None:
        imageIOCache = imageIOCache.text
    if pngAcceleration is not None:
        pngAcceleration = pngAcceleration.text
    if jpegAcceleration is not None:
        jpegAcceleration = jpegAcceleration.text
    if allowNativeMosaic is not None:
        allowNativeMosaic = allowNativeMosaic.text
    return _jai(allowInterpolation, recycling, tilePriority, tileThreads, memoryCapacity, memoryThreshold, imageIOCache, pngAcceleration, jpegAcceleration, allowNativeMosaic)

def _write_jai(builder, jai):
    builder.start("jai", dict())
    if jai.allowInterpolation is not None:
        builder.start("allowInterpolation", dict())
        builder.data(jai.allowInterpolation)
        builder.end("allowInterpolation")
    if jai.recycling is not None:
        builder.start("recycling", dict())
        builder.data(jai.allowInterpolation)
        builder.end("recycling")
    if jai.tilePriority is not None:
        builder.start("tilePriority", dict())
        builder.data(jai.tilePriority)
        builder.end("tilePriority")
    if jai.tileThreads is not None:
        builder.start("tileThreads", dict())
        builder.data(jai.tileThreads)
        builder.end("tileThreads")
    if jai.memoryCapacity is not None:
        builder.start("memoryCapacity", dict())
        builder.data(jai.memoryCapacity)
        builder.end("memoryCapacity")
    if jai.memoryThreshold is not None:
        builder.start("memoryThreshold", dict())
        builder.data(jai.memoryThreshold)
        builder.end("memoryThreshold")
    if jai.imageIOCache is not None:
        builder.start("imageIOCache", dict())
        builder.data(jai.imageIOCache)
        builder.end("imageIOCache")
    if jai.pngAcceleration is not None:
        builder.start("pngAcceleration", dict())
        builder.data(jai.pngAcceleration)
        builder.end("pngAcceleration")
    if jai.jpegAcceleration is not None:
        builder.start("jpegAcceleration", dict())
        builder.data(jai.jpegAcceleration)
        builder.end("jpegAcceleration")
    if jai.tileThreads is not None:
        builder.start("allowNativeMosaic", dict())
        builder.data(jai.allowNativeMosaic)
        builder.end("allowNativeMosaic")
    builder.end("jai")

class _coverageAccess(object):
    def __init__(self, maxPoolSize, corePoolSize, keepAliveTime, queueType, imageIOCacheThreshold):
        self.maxPoolSize = maxPoolSize
        self.corePoolSize = corePoolSize
        self.keepAliveTime = keepAliveTime
        self.queueType = queueType
        self.imageIOCacheThreshold = imageIOCacheThreshold

def _read_coverageAccess(node):
    maxPoolSize = node.find("maxPoolSize")
    corePoolSize = node.find("corePoolSize")
    keepAliveTime = node.find("keepAliveTime")
    queueType = node.find("queueType")
    imageIOCacheThreshold = node.find("imageIOCacheThreshold")

    if maxPoolSize is not None:
        maxPoolSize = maxPoolSize.text
    if corePoolSize is not None:
        corePoolSize = corePoolSize.text
    if keepAliveTime is not None:
        keepAliveTime = keepAliveTime.text
    if queueType is not None:
        queueType = queueType.text
    if imageIOCacheThreshold is not None:
        imageIOCacheThreshold = imageIOCacheThreshold.text

    return _coverageAccess(maxPoolSize, corePoolSize, keepAliveTime, queueType, imageIOCacheThreshold)

def _write_coverageAccess(builder, coverageAccess):
    builder.start("coverageAccess", dict())
    if coverageAccess.maxPoolSize is not None:
        builder.start("maxPoolSize", dict())
        builder.data(coverageAccess.maxPoolSize)
        builder.end("maxPoolSize")
    if coverageAccess.corePoolSize is not None:
        builder.start("corePoolSize", dict())
        builder.data(coverageAccess.corePoolSize)
        builder.end("corePoolSize")
    if coverageAccess.keepAliveTime is not None:
        builder.start("keepAliveTime", dict())
        builder.data(coverageAccess.keepAliveTime)
        builder.end("keepAliveTime")
    if coverageAccess.maxPoolSize is not None:
        builder.start("queueType", dict())
        builder.data(coverageAccess.queueType)
        builder.end("queueType")
    if coverageAccess.imageIOCacheThreshold is not None:
        builder.start("imageIOCacheThreshold", dict())
        builder.data(coverageAccess.imageIOCacheThreshold)
        builder.end("imageIOCacheThreshold")
    builder.end("coverageAccess")
    

def settings_from_index(catalog, node):
    return Settings(catalog)

class Settings(ResourceInfo): 
    resource_type = "global"
    save_method = "PUT"

    def __init__(self, catalog):
        super(Settings, self).__init__()
        self.catalog = catalog

    @property
    def href(self):
        return "%s/settings.xml" % (self.catalog.service_url)

    settings = xml_property("settings", _read_settings)
    contact = xml_property("contact", _read_contact)
    jai = xml_property("jai", _read_jai)
    coverageAccess = xml_property("coverageAccess", _read_coverageAccess)
    updateSequence = xml_property("updateSequence")
    featureTypeCacheSize = xml_property("featureTypeCacheSize")
    globalServices = xml_property("globalServices")
    xmlPostRequestLogBufferSize = xml_property("xmlPostRequestLogBufferSize")

    writers = dict(
                settings = _write_settings,
                contact = _write_contact,
                jai = _write_jai,
                coverageAccess = _write_coverageAccess,
                updateSequence = write_string("updateSequence"),
                featureTypeCacheSize = write_string("featureTypeCacheSize"),
                globalServices = write_bool("globalServices"),
                xmlPostRequestLogBufferSize = write_string("xmlPostRequestLogBufferSize"),
            )

    def __repr__(self):
        return "settings @ %s" % (self.href)

def wms_settings_from_index(catalog, node):
    return WmsInfo(catalog)

class WmsInfo(ResourceInfo):
    resource_type = "wmsinfo"
    save_method = "PUT"
    
    def __init__(self, catalog):
        super(WmsInfo, self).__init__()
        self.catalog = catalog
   
    # Need to modify this for potential use with Workspace local WMS 
    @property
    def href(self):
        return "%s/services/wms/settings.xml" % (self.catalog.service_url)

    enabled = xml_property("enabled")
    name = xml_property("name")
    title = xml_property("title")
    abstrct = xml_property("abstrct") # Spelled wrong on geoserver side
    maintainer = xml_property("maintainer")
    keywords = xml_property("keywords", string_list)
    accessConstraints = xml_property("accessConstraints")
    fees = xml_property("fees")
    citeCompliant = xml_property("citeCompliant")
    onlineResource = xml_property("onlineResource")
    schemaBaseURL = xml_property("schemaBaseURL")
    verbose = xml_property("verbose")
    interpolation = xml_property("interpolation")
    maxBuffer = xml_property("maxBuffer")
    maxRequestMemory = xml_property("maxRequestMemory")
    maxRenderingTime = xml_property("maxRenderingTime")
    maxRenderingErrors = xml_property("maxRenderingErrors")
    metadata = xml_property("metadata", key_value_pairs)

    # Authority URLs
    # Root Layer Identifiers
    # Limited SRS List

    writers = dict(
                enabled = write_bool("enabled"),
                name = write_string("name"),
                title = write_string("title"),
                abstrct = write_string("abstrct"),
                maintainer = write_string("maintainer"),
                keywords = write_string_list("keywords"), 
                accessConstraints = write_string("accessConstraints"),
                fees = write_string("fees"),
                citeCompliant = write_string("citeCompliant"),
                onlineResource = write_string("onlineResource"),
                schemaBaseURL = write_string("schemaBaseURL"),
                verbose = write_string("verbose"),
                interpolation = write_string("interpolation"),
                maxBuffer = write_string("maxBuffer"),
                maxRequestMemory = write_string("maxRequestMemory"),
                maxRenderingTime = write_string("maxRenderingTime"),
                maxRenderingErrors = write_string("maxRenderingErrors"),
                metadata = write_dict("metadata"),
            )

    def __repr__(self):
        return "wms settings @ %s" % (self.href) 
