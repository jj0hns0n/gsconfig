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
    jai = xml_property("jai", _read_jai)
    coverageAccess = xml_property("coverageAccess", _read_coverageAccess)
    updateSequence = xml_property("updateSequence")
    featureTypeCacheSize = xml_property("featureTypeCacheSize")
    globalServices = xml_property("globalServices")
    xmlPostRequestLogBufferSize = xml_property("xmlPostRequestLogBufferSize")

    writers = dict(
                settings = _write_settings,
                jai = _write_jai,
                coverageAccess = _write_coverageAccess,
                updateSequence = write_string("updateSequence"),
                featureTypeCacheSize = write_string("featureTypeCacheSize"),
                globalServices = write_bool("globalServices"),
                xmlPostRequestLogBufferSize = write_string("xmlPostRequestLogBufferSize"),
            )

    def __repr__(self):
        return "settings @ %s" % (self.href)

def contactinfo_from_index(catalog, node):
    return Contact(catalog)

class Contact(ResourceInfo):
    resource_type = "contact"
    save_method = "PUT"
    
    def __init__(self, catalog):
        super(Contact, self).__init__()
        self.catalog = catalog

    @property
    def href(self):
        return "%s/settings/contact.xml" % (self.catalog.service_url)

    address = xml_property("address")
    addressCity = xml_property("addressCity")
    addressCountry = xml_property("addressCountry")
    addressPostalCode = xml_property("addressPostalCode")
    addressState = xml_property("addressState")
    addressType = xml_property("addressType")
    contactEmail = xml_property("contactEmail")
    contactFacsimile = xml_property("contactFacsimile")
    contactOrganization = xml_property("contactOrganization")
    contactPerson = xml_property("contactPerson")
    contactPosition = xml_property("contactPosition")
    contactVoice = xml_property("contactVoice")

    writers = dict(
        address = write_string("address"),
        addressCity = write_string("addressCity"),
        addressCountry = write_string("addressCountry"),
        addressPostalCode = write_string("addressPostalCode"),
        addressState = write_string("addressState"),
        addressType = write_string("addressType"),
        contactEmail = write_string("contactEmail"),
        contactFacsimile = write_string("contactFacsimile"),
        contactOrganization = write_string("contactOrganization"),
        contactPerson = write_string("contactPerson"),
        contactPosition = write_string("contactPosition"),
        contactVoice = write_string("contactVoice")
    )

    def __repr__(self):
        return "contactinfo @ %s" % (self.href)


def wms_settings_from_index(catalog, node):
    return WmsInfo(catalog)

class WmsInfo(ResourceInfo):
    resource_type = "wms"
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
