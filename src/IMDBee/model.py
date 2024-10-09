import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


model = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
model -= sgqlc.types.relay.Node
model -= sgqlc.types.relay.PageInfo


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
class ActionLinkName(sgqlc.types.Scalar):
    __schema__ = model


class AdvancedNameSearchSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BIRTH_DATE`None
    * `DEATH_DATE`None
    * `NAME`None
    * `POPULARITY`None
    '''
    __schema__ = model
    __choices__ = ('BIRTH_DATE', 'DEATH_DATE', 'NAME', 'POPULARITY')


class AdvancedTitleSearchSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BOX_OFFICE_GROSS_DOMESTIC`None
    * `METACRITIC_SCORE`None
    * `MY_RATING`None
    * `MY_RATING_DATE`None
    * `POPULARITY`None
    * `RANKING`None
    * `RELEASE_DATE`None
    * `RUNTIME`None
    * `SINGLE_USER_RATING`None
    * `SINGLE_USER_RATING_DATE`None
    * `TITLE_REGIONAL`None
    * `USER_RATING`None
    * `USER_RATING_COUNT`None
    * `YEAR`None
    '''
    __schema__ = model
    __choices__ = ('BOX_OFFICE_GROSS_DOMESTIC', 'METACRITIC_SCORE', 'MY_RATING', 'MY_RATING_DATE', 'POPULARITY', 'RANKING', 'RELEASE_DATE', 'RUNTIME', 'SINGLE_USER_RATING', 'SINGLE_USER_RATING_DATE', 'TITLE_REGIONAL', 'USER_RATING', 'USER_RATING_COUNT', 'YEAR')


class Age(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `AGE_18_29`None
    * `AGE_30_44`None
    * `AGE_45_PLUS`None
    * `AGE_UNDER_18`None
    '''
    __schema__ = model
    __choices__ = ('AGE_18_29', 'AGE_30_44', 'AGE_45_PLUS', 'AGE_UNDER_18')


class AkaFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DISPLAY_TITLES_ONLY`None
    * `EXCLUDE_IF_SAME_AS_PRIMARY`None
    '''
    __schema__ = model
    __choices__ = ('DISPLAY_TITLES_ONLY', 'EXCLUDE_IF_SAME_AS_PRIMARY')


class AkaSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `COUNTRY`None
    * `RELEVANCE`None
    '''
    __schema__ = model
    __choices__ = ('COUNTRY', 'RELEVANCE')


class ArchivedOrUnarchivedFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL_CREDITS`None
    * `ARCHIVED_ONLY`None
    * `UNARCHIVED_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('ALL_CREDITS', 'ARCHIVED_ONLY', 'UNARCHIVED_ONLY')


class AttachmentGroup(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CAST`None
    * `CASTING_DIRECTORS`None
    * `FILMMAKERS`None
    * `WRITERS`None
    '''
    __schema__ = model
    __choices__ = ('CAST', 'CASTING_DIRECTORS', 'FILMMAKERS', 'WRITERS')


class AuthProviderType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `AMAZON`None
    * `APPLE`None
    * `FB`None
    * `GOOGLE`None
    '''
    __schema__ = model
    __choices__ = ('AMAZON', 'APPLE', 'FB', 'GOOGLE')


class AwardNominationsSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `PRESTIGIOUS`None
    '''
    __schema__ = model
    __choices__ = ('PRESTIGIOUS',)


class AwardWinnerSearchFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `NON_WINNER_ONLY`None
    * `WINNER_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('NON_WINNER_ONLY', 'WINNER_ONLY')


Boolean = sgqlc.types.Boolean

class BoxOfficeArea(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DOMESTIC`None
    * `INTERNATIONAL`None
    * `WORLDWIDE`None
    '''
    __schema__ = model
    __choices__ = ('DOMESTIC', 'INTERNATIONAL', 'WORLDWIDE')


class ChartNameType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MOST_POPULAR_NAMES`None
    '''
    __schema__ = model
    __choices__ = ('MOST_POPULAR_NAMES',)


class ChartTitleType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `LOWEST_RATED_MOVIES`None
    * `MOST_POPULAR_MOVIES`None
    * `MOST_POPULAR_TV_SHOWS`None
    * `TOP_RATED_ENGLISH_MOVIES`None
    * `TOP_RATED_INDIAN_MOVIES`None
    * `TOP_RATED_MALAYALAM_MOVIES`None
    * `TOP_RATED_MOVIES`None
    * `TOP_RATED_TAMIL_MOVIES`None
    * `TOP_RATED_TELUGU_MOVIES`None
    * `TOP_RATED_TV_SHOWS`None
    '''
    __schema__ = model
    __choices__ = ('LOWEST_RATED_MOVIES', 'MOST_POPULAR_MOVIES', 'MOST_POPULAR_TV_SHOWS', 'TOP_RATED_ENGLISH_MOVIES', 'TOP_RATED_INDIAN_MOVIES', 'TOP_RATED_MALAYALAM_MOVIES', 'TOP_RATED_MOVIES', 'TOP_RATED_TAMIL_MOVIES', 'TOP_RATED_TELUGU_MOVIES', 'TOP_RATED_TV_SHOWS')


class ClaimedNameStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BLOCKED`None
    * `CLAIMED`None
    * `NOT_REQUESTED`None
    * `PENDING_APPROVAL`None
    * `PENDING_CREATION`None
    * `PREVIOUS_CLAIMED`None
    * `UNKNOWN`None
    '''
    __schema__ = model
    __choices__ = ('BLOCKED', 'CLAIMED', 'NOT_REQUESTED', 'PENDING_APPROVAL', 'PENDING_CREATION', 'PREVIOUS_CLAIMED', 'UNKNOWN')


class ColorationType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ACES`None
    * `BLACK_AND_WHITE`None
    * `COLOR`None
    * `COLORIZED`None
    '''
    __schema__ = model
    __choices__ = ('ACES', 'BLACK_AND_WHITE', 'COLOR', 'COLORIZED')


class ComingSoonSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `POPULARITY`None
    * `RELEASE_DATE`None
    '''
    __schema__ = model
    __choices__ = ('POPULARITY', 'RELEASE_DATE')


class ComingSoonType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MOVIE`None
    * `TV`None
    * `TV_EPISODE`None
    '''
    __schema__ = model
    __choices__ = ('MOVIE', 'TV', 'TV_EPISODE')


class CompanyKnownForStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ACTIVE`None
    * `BLOCKED`None
    '''
    __schema__ = model
    __choices__ = ('ACTIVE', 'BLOCKED')


class ConsentOperation(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CUSTOM`None
    * `IN`None
    * `OUT`None
    '''
    __schema__ = model
    __choices__ = ('CUSTOM', 'IN', 'OUT')


class ConsentType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `THIRD_PARTY_DATA_SHARING`None
    * `TRACKING_COOKIE`None
    '''
    __schema__ = model
    __choices__ = ('THIRD_PARTY_DATA_SHARING', 'TRACKING_COOKIE')


class ContentRestrictionReason(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `PRO_ANNOUNCED_TITLE`None
    * `PRO_IN_DEV_TITLE`None
    '''
    __schema__ = model
    __choices__ = ('PRO_ANNOUNCED_TITLE', 'PRO_IN_DEV_TITLE')


class ContributorLeaderboardPeriodTypeId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL_TIME`None
    * `MONTH`None
    * `YEAR`None
    '''
    __schema__ = model
    __choices__ = ('ALL_TIME', 'MONTH', 'YEAR')


class ContributorRankSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `APPROVED_ITEMS_DELTA`None
    * `RANK`None
    * `RANK_DELTA`None
    '''
    __schema__ = model
    __choices__ = ('APPROVED_ITEMS_DELTA', 'RANK', 'RANK_DELTA')


class Country(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `AD`None
    * `AE`None
    * `AF`None
    * `AG`None
    * `AI`None
    * `AL`None
    * `AM`None
    * `AN`None
    * `AO`None
    * `AQ`None
    * `AR`None
    * `AS`None
    * `AT`None
    * `AU`None
    * `AW`None
    * `AX`None
    * `AZ`None
    * `BA`None
    * `BB`None
    * `BD`None
    * `BE`None
    * `BF`None
    * `BG`None
    * `BH`None
    * `BI`None
    * `BJ`None
    * `BL`None
    * `BM`None
    * `BN`None
    * `BO`None
    * `BQ`None
    * `BR`None
    * `BS`None
    * `BT`None
    * `BV`None
    * `BW`None
    * `BY`None
    * `BZ`None
    * `CA`None
    * `CC`None
    * `CD`None
    * `CF`None
    * `CG`None
    * `CH`None
    * `CI`None
    * `CK`None
    * `CL`None
    * `CM`None
    * `CN`None
    * `CO`None
    * `CR`None
    * `CS`None
    * `CU`None
    * `CV`None
    * `CW`None
    * `CX`None
    * `CY`None
    * `CZ`None
    * `DE`None
    * `DJ`None
    * `DK`None
    * `DM`None
    * `DO`None
    * `DZ`None
    * `EC`None
    * `EE`None
    * `EG`None
    * `EH`None
    * `ER`None
    * `ES`None
    * `ET`None
    * `FI`None
    * `FJ`None
    * `FK`None
    * `FM`None
    * `FO`None
    * `FR`None
    * `GA`None
    * `GB`None
    * `GD`None
    * `GE`None
    * `GF`None
    * `GG`None
    * `GH`None
    * `GI`None
    * `GL`None
    * `GM`None
    * `GN`None
    * `GP`None
    * `GQ`None
    * `GR`None
    * `GS`None
    * `GT`None
    * `GU`None
    * `GW`None
    * `GY`None
    * `HK`None
    * `HM`None
    * `HN`None
    * `HR`None
    * `HT`None
    * `HU`None
    * `ID`None
    * `IE`None
    * `IL`None
    * `IM`None
    * `IN`None
    * `IO`None
    * `IQ`None
    * `IR`None
    * `IS`None
    * `IT`None
    * `JE`None
    * `JM`None
    * `JO`None
    * `JP`None
    * `KE`None
    * `KG`None
    * `KH`None
    * `KI`None
    * `KM`None
    * `KN`None
    * `KP`None
    * `KR`None
    * `KW`None
    * `KY`None
    * `KZ`None
    * `LA`None
    * `LB`None
    * `LC`None
    * `LI`None
    * `LK`None
    * `LR`None
    * `LS`None
    * `LT`None
    * `LU`None
    * `LV`None
    * `LY`None
    * `MA`None
    * `MC`None
    * `MD`None
    * `ME`None
    * `MF`None
    * `MG`None
    * `MH`None
    * `MK`None
    * `ML`None
    * `MM`None
    * `MN`None
    * `MO`None
    * `MP`None
    * `MQ`None
    * `MR`None
    * `MS`None
    * `MT`None
    * `MU`None
    * `MV`None
    * `MW`None
    * `MX`None
    * `MY`None
    * `MZ`None
    * `NA`None
    * `NC`None
    * `NE`None
    * `NF`None
    * `NG`None
    * `NI`None
    * `NL`None
    * `NO`None
    * `NON_US`None
    * `NP`None
    * `NR`None
    * `NU`None
    * `NZ`None
    * `OM`None
    * `PA`None
    * `PE`None
    * `PF`None
    * `PG`None
    * `PH`None
    * `PK`None
    * `PL`None
    * `PM`None
    * `PN`None
    * `PR`None
    * `PS`None
    * `PT`None
    * `PW`None
    * `PY`None
    * `QA`None
    * `RE`None
    * `RO`None
    * `RS`None
    * `RU`None
    * `RW`None
    * `SA`None
    * `SB`None
    * `SC`None
    * `SD`None
    * `SE`None
    * `SG`None
    * `SH`None
    * `SI`None
    * `SJ`None
    * `SK`None
    * `SL`None
    * `SM`None
    * `SN`None
    * `SO`None
    * `SR`None
    * `SS`None
    * `ST`None
    * `SV`None
    * `SX`None
    * `SY`None
    * `SZ`None
    * `TC`None
    * `TD`None
    * `TF`None
    * `TG`None
    * `TH`None
    * `TJ`None
    * `TK`None
    * `TL`None
    * `TM`None
    * `TN`None
    * `TO`None
    * `TR`None
    * `TT`None
    * `TV`None
    * `TW`None
    * `TZ`None
    * `UA`None
    * `UG`None
    * `UM`None
    * `US`None
    * `UY`None
    * `UZ`None
    * `VA`None
    * `VC`None
    * `VE`None
    * `VG`None
    * `VI`None
    * `VN`None
    * `VU`None
    * `WF`None
    * `WS`None
    * `YE`None
    * `YT`None
    * `ZA`None
    * `ZM`None
    * `ZW`None
    '''
    __schema__ = model
    __choices__ = ('AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CS', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NON_US', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW')


class CreditedOrUncreditedFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL_CREDITS`None
    * `CREDITED_ONLY`None
    * `UNCREDITED_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('ALL_CREDITS', 'CREDITED_ONLY', 'UNCREDITED_ONLY')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DemographicDataTypeValue(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BIRTH_DATE`None
    * `BIRTH_YEAR`None
    * `CITIZENSHIP`None
    * `DISABILITY`None
    * `ETHNICITY`None
    * `GENDER_IDENTITY`None
    * `IDENTIFIES_AS_DISABLED`None
    * `IDENTIFIES_AS_TRANSGENDER`None
    * `NATIONALITY`None
    * `PRONOUN`None
    * `SEXUAL_ORIENTATION`None
    '''
    __schema__ = model
    __choices__ = ('BIRTH_DATE', 'BIRTH_YEAR', 'CITIZENSHIP', 'DISABILITY', 'ETHNICITY', 'GENDER_IDENTITY', 'IDENTIFIES_AS_DISABLED', 'IDENTIFIES_AS_TRANSGENDER', 'NATIONALITY', 'PRONOUN', 'SEXUAL_ORIENTATION')


class EpisodesSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EPISODE_THEN_RELEASE`None
    * `RATING`None
    * `RELEASE_DATE`None
    '''
    __schema__ = model
    __choices__ = ('EPISODE_THEN_RELEASE', 'RATING', 'RELEASE_DATE')


class Experimental_NumericThresholdComparator(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Equal`None
    * `GreaterThan`None
    * `GreaterThanOrEqual`None
    * `LessThan`None
    * `LessThanOrEqual`None
    '''
    __schema__ = model
    __choices__ = ('Equal', 'GreaterThan', 'GreaterThanOrEqual', 'LessThan', 'LessThanOrEqual')


class Experimental_UIWorkflowActionType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Cancel`None
    * `Other`None
    * `Primary`None
    * `Secondary`None
    * `Submit`None
    '''
    __schema__ = model
    __choices__ = ('Cancel', 'Other', 'Primary', 'Secondary', 'Submit')


class Experimental_UIWorkflowFeedbackType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BlockingError`None
    * `Information`None
    * `Warning`None
    '''
    __schema__ = model
    __choices__ = ('BlockingError', 'Information', 'Warning')


class Experimental_UIWorkflowFormInputType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Checkbox`None
    * `Radio`None
    * `Text`None
    '''
    __schema__ = model
    __choices__ = ('Checkbox', 'Radio', 'Text')


class Experimental_UIWorkflowGlobalMenuItemLinkType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Navigation`None
    '''
    __schema__ = model
    __choices__ = ('Navigation',)


class Experimental_UIWorkflowItemActionType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Add`None
    * `Delete`None
    * `Discard`None
    * `Edit`None
    * `Navigate`None
    * `Report`None
    '''
    __schema__ = model
    __choices__ = ('Add', 'Delete', 'Discard', 'Edit', 'Navigate', 'Report')


class Experimental_UIWorkflowSubjectType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Company`None
    * `Name`None
    * `Other`None
    * `Title`None
    '''
    __schema__ = model
    __choices__ = ('Company', 'Name', 'Other', 'Title')


class Experimental_UIWorkflowType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Add`None
    * `Delete`None
    * `Edit`None
    * `Other`None
    * `Report`None
    '''
    __schema__ = model
    __choices__ = ('Add', 'Delete', 'Edit', 'Other', 'Report')


class Experimental_UploadMediaType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `IMAGE`None
    '''
    __schema__ = model
    __choices__ = ('IMAGE',)


class ExplicitContentFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_ADULT`None
    * `INCLUDE_ADULT`None
    * `ONLY_ADULT`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_ADULT', 'INCLUDE_ADULT', 'ONLY_ADULT')


class ExportSortByField(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `STARTED_ON`None
    '''
    __schema__ = model
    __choices__ = ('STARTED_ON',)


class ExportStatusId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `FAILED`None
    * `PROCESSING`None
    * `READY`None
    * `UNAUTHORIZED`None
    '''
    __schema__ = model
    __choices__ = ('FAILED', 'PROCESSING', 'READY', 'UNAUTHORIZED')


class ExportType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `LIST`None
    * `RATINGS`None
    '''
    __schema__ = model
    __choices__ = ('LIST', 'RATINGS')


class FeaturedImagesOption(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_FEATURED`None
    * `FEATURED_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_FEATURED', 'FEATURED_ONLY')


class FeedbackGivenFeatureType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CONSUMER_ADVANCED_SEARCH_RESULTS`None
    * `CONSUMER_MAIN_SEARCH_RESULTS`None
    '''
    __schema__ = model
    __choices__ = ('CONSUMER_ADVANCED_SEARCH_RESULTS', 'CONSUMER_MAIN_SEARCH_RESULTS')


class FilterInclusion(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE`None
    * `INCLUDE`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE', 'INCLUDE')


class FilterSpoilers(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_SPOILERS`None
    * `SPOILERS_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_SPOILERS', 'SPOILERS_ONLY')


class FilterVersions(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL_VERSIONS`None
    * `ORIGINAL_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('ALL_VERSIONS', 'ORIGINAL_ONLY')


Float = sgqlc.types.Float

class Gender(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `FEMALE`None
    * `MALE`None
    '''
    __schema__ = model
    __choices__ = ('FEMALE', 'MALE')


class GenreSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DEFAULT`None
    * `RELEVANCE`None
    '''
    __schema__ = model
    __choices__ = ('DEFAULT', 'RELEVANCE')


class GuildAffiliationVisibilityLevel(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `IMDB_PRO_ONLY`None
    * `PUBLIC`None
    '''
    __schema__ = model
    __choices__ = ('IMDB_PRO_ONLY', 'PUBLIC')


class GuildDataVerificationType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `SELF_VERIFIED`None
    * `THIRD_PARTY_VERIFIED`None
    '''
    __schema__ = model
    __choices__ = ('SELF_VERIFIED', 'THIRD_PARTY_VERIFIED')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class InterestVisibilityLevel(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HIDDEN`None
    * `PUBLIC`None
    '''
    __schema__ = model
    __choices__ = ('HIDDEN', 'PUBLIC')


class KnownForPreference(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `AUTOMATIC`None
    * `CUSTOM`None
    '''
    __schema__ = model
    __choices__ = ('AUTOMATIC', 'CUSTOM')


class Language(sgqlc.types.Scalar):
    __schema__ = model


class LengthUnit(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CENTIMETER`None
    * `METER`None
    '''
    __schema__ = model
    __choices__ = ('CENTIMETER', 'METER')


class ListClassId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CHECK_INS`None
    * `FAVORITE_ACTORS`None
    * `FAVORITE_THEATRES`None
    * `INTERNAL`None
    * `LIST`None
    * `NOT_INTERESTED`None
    * `PRO_LIST`None
    * `SEEN`None
    * `WATCH_LIST`None
    '''
    __schema__ = model
    __choices__ = ('CHECK_INS', 'FAVORITE_ACTORS', 'FAVORITE_THEATRES', 'INTERNAL', 'LIST', 'NOT_INTERESTED', 'PRO_LIST', 'SEEN', 'WATCH_LIST')


class ListInteractionCountTimeRange(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL_TIME`None
    * `ONE_WEEK`None
    '''
    __schema__ = model
    __choices__ = ('ALL_TIME', 'ONE_WEEK')


class ListItemSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CREATED_DATE`None
    * `LIST_ORDER`None
    * `MODIFIED_DATE`None
    * `POPULARITY`None
    '''
    __schema__ = model
    __choices__ = ('CREATED_DATE', 'LIST_ORDER', 'MODIFIED_DATE', 'POPULARITY')


class ListSearchSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DATE_CREATED`None
    * `DATE_MODIFIED`None
    * `NAME`None
    '''
    __schema__ = model
    __choices__ = ('DATE_CREATED', 'DATE_MODIFIED', 'NAME')


class ListTypeId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `GALLERIES`None
    * `IMAGES`None
    * `LISTS`None
    * `PEOPLE`None
    * `THEATRES`None
    * `TITLES`None
    * `VIDEOS`None
    '''
    __schema__ = model
    __choices__ = ('GALLERIES', 'IMAGES', 'LISTS', 'PEOPLE', 'THEATRES', 'TITLES', 'VIDEOS')


class ListVisibilityId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `PRIVATE`None
    * `PUBLIC`None
    '''
    __schema__ = model
    __choices__ = ('PRIVATE', 'PUBLIC')


class LocationDecimal(sgqlc.types.Scalar):
    __schema__ = model


class MainSearchTitleType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MOVIE`None
    * `MUSIC_VIDEO`None
    * `PODCAST_EPISODE`None
    * `PODCAST_SERIES`None
    * `TV`None
    * `TV_EPISODE`None
    * `VIDEO_GAME`None
    '''
    __schema__ = model
    __choices__ = ('MOVIE', 'MUSIC_VIDEO', 'PODCAST_EPISODE', 'PODCAST_SERIES', 'TV', 'TV_EPISODE', 'VIDEO_GAME')


class MainSearchType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `COMPANY`None
    * `INTEREST`None
    * `KEYWORD`None
    * `NAME`None
    * `TITLE`None
    '''
    __schema__ = model
    __choices__ = ('COMPANY', 'INTEREST', 'KEYWORD', 'NAME', 'TITLE')


class ManagedClientStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CAN_REQUEST`None
    * `ENABLED`None
    * `REQUESTED`None
    '''
    __schema__ = model
    __choices__ = ('CAN_REQUEST', 'ENABLED', 'REQUESTED')


class ManagingRepresentativeStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DISABLED`None
    * `ENABLED`None
    '''
    __schema__ = model
    __choices__ = ('DISABLED', 'ENABLED')


class MaturityLevel(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `INCLUDE_MATURE`None
    '''
    __schema__ = model
    __choices__ = ('INCLUDE_MATURE',)


class MeterRankChangeDirection(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DOWN`None
    * `FLAT`None
    * `UP`None
    '''
    __schema__ = model
    __choices__ = ('DOWN', 'FLAT', 'UP')


class MonthDay(sgqlc.types.Scalar):
    __schema__ = model


class MyFavoriteTheaterSearchFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ONLY_MY_FAVORITE`None
    '''
    __schema__ = model
    __choices__ = ('ONLY_MY_FAVORITE',)


class MyRatingSearchFilterType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE`None
    * `INCLUDE`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE', 'INCLUDE')


class NameChartRankingsType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `INDIA_STAR_METER`None
    '''
    __schema__ = model
    __choices__ = ('INDIA_STAR_METER',)


class NameCreditSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `RELEASE_DATE`None
    '''
    __schema__ = model
    __choices__ = ('RELEASE_DATE',)


class NameDataType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `AWARD_NOMINATIONS`None
    * `BIOGRAPHY`None
    * `BIRTH_DATE`None
    * `BIRTH_PLACE`None
    * `DEATH_DATE`None
    * `DEATH_PLACE`None
    * `HEIGHT_INFO`None
    * `QUOTES`None
    * `TRIVIA`None
    '''
    __schema__ = model
    __choices__ = ('AWARD_NOMINATIONS', 'BIOGRAPHY', 'BIRTH_DATE', 'BIRTH_PLACE', 'DEATH_DATE', 'DEATH_PLACE', 'HEIGHT_INFO', 'QUOTES', 'TRIVIA')


class NameDeathStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALIVE`None
    * `DEAD`None
    * `PRESUMED_DEAD`None
    '''
    __schema__ = model
    __choices__ = ('ALIVE', 'DEAD', 'PRESUMED_DEAD')


class NameDisplayVisibilityLevel(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HIDDEN`None
    * `PUBLIC`None
    '''
    __schema__ = model
    __choices__ = ('HIDDEN', 'PUBLIC')


class NameFacetField(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `GENDER_IDENTITY`None
    * `JOB_CATEGORIES`None
    '''
    __schema__ = model
    __choices__ = ('GENDER_IDENTITY', 'JOB_CATEGORIES')


class NameGenderIdentity(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `FEMALE`None
    * `MALE`None
    * `NON_BINARY`None
    * `OTHER`None
    '''
    __schema__ = model
    __choices__ = ('FEMALE', 'MALE', 'NON_BINARY', 'OTHER')


class NameListSearchSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BIRTH_DATE`None
    * `DATE_ADDED`None
    * `DEATH_DATE`None
    * `LIST_ORDER`None
    * `NAME`None
    * `POPULARITY`None
    '''
    __schema__ = model
    __choices__ = ('BIRTH_DATE', 'DATE_ADDED', 'DEATH_DATE', 'LIST_ORDER', 'NAME', 'POPULARITY')


class NameNetworkAlgorithmType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MOST_CONNECTIONS`None
    * `STRONGEST_MUTUAL`None
    '''
    __schema__ = model
    __choices__ = ('MOST_CONNECTIONS', 'STRONGEST_MUTUAL')


class NewsCategory(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CELEBRITY`None
    * `INDIE`None
    * `MOVIE`None
    * `TOP`None
    * `TV`None
    '''
    __schema__ = model
    __choices__ = ('CELEBRITY', 'INDIE', 'MOVIE', 'TOP', 'TV')


class NominationsSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `PRESTIGIOUS`None
    * `WINS`None
    '''
    __schema__ = model
    __choices__ = ('PRESTIGIOUS', 'WINS')


class PlatformId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ANDROID`None
    * `ANDROID_FIRE`None
    * `FIRE_TV_DETAIL`None
    * `IOS`None
    * `MOBILE_WEB`None
    * `WEB`None
    '''
    __schema__ = model
    __choices__ = ('ANDROID', 'ANDROID_FIRE', 'FIRE_TV_DETAIL', 'IOS', 'MOBILE_WEB', 'WEB')


class PlatformLinkFormatId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ANDROID`None
    * `ANDROID_FIRE`None
    * `FIRE_TV_DETAIL`None
    * `IOS`None
    * `MDOT`None
    * `WEB`None
    '''
    __schema__ = model
    __choices__ = ('ANDROID', 'ANDROID_FIRE', 'FIRE_TV_DETAIL', 'IOS', 'MDOT', 'WEB')


class PlotType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `OUTLINE`None
    * `SUMMARY`None
    * `SYNOPSIS`None
    '''
    __schema__ = model
    __choices__ = ('OUTLINE', 'SUMMARY', 'SYNOPSIS')


class PrivacyPromptType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CONSENT_PRIMARY`None
    '''
    __schema__ = model
    __choices__ = ('CONSENT_PRIMARY',)


class ProductionStageFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ABANDONED`None
    * `COMPLETED`None
    * `IN_DEVELOPMENT`None
    * `IN_PRODUCTION`None
    * `POST_PRODUCTION`None
    * `PRE_PRODUCTION`None
    * `RELEASED`None
    '''
    __schema__ = model
    __choices__ = ('ABANDONED', 'COMPLETED', 'IN_DEVELOPMENT', 'IN_PRODUCTION', 'POST_PRODUCTION', 'PRE_PRODUCTION', 'RELEASED')


class ProfessionsFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_PRIMARY_PROFESSIONS`None
    * `PRIMARY_PROFESSIONS_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_PRIMARY_PROFESSIONS', 'PRIMARY_PROFESSIONS_ONLY')


class PromptType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `RATINGS_TITLE_MAIN`None
    * `RATINGS_TITLE_TRIVIA`None
    '''
    __schema__ = model
    __choices__ = ('RATINGS_TITLE_MAIN', 'RATINGS_TITLE_TRIVIA')


class PublicationStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `NOT_PUBLISHED`None
    * `PUBLISHED`None
    * `REDIRECTED`None
    '''
    __schema__ = model
    __choices__ = ('NOT_PUBLISHED', 'PUBLISHED', 'REDIRECTED')


class RankChangeDirection(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DOWN`None
    * `FLAT`None
    * `UP`None
    '''
    __schema__ = model
    __choices__ = ('DOWN', 'FLAT', 'UP')


class RankedTitleListType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `LOWEST_RATED_MOVIES`None
    * `MOVIE_METER`None
    * `TITLE_METER`None
    * `TOP_RATED_MOVIES`None
    * `TV_METER`None
    '''
    __schema__ = model
    __choices__ = ('LOWEST_RATED_MOVIES', 'MOVIE_METER', 'TITLE_METER', 'TOP_RATED_MOVIES', 'TV_METER')


class RatingsCondition(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EQUALS`None
    '''
    __schema__ = model
    __choices__ = ('EQUALS',)


class RatingsPrivacySetting(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `PRIVATE`None
    * `PUBLIC`None
    * `PUBLIC_WITH_REVIEWS`None
    '''
    __schema__ = model
    __choices__ = ('PRIVATE', 'PUBLIC', 'PUBLIC_WITH_REVIEWS')


class RatingsSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MOST_RECENT`None
    * `TOP_RATED`None
    '''
    __schema__ = model
    __choices__ = ('MOST_RECENT', 'TOP_RATED')


class ReactionsGroupSelectionType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MULTIPLE`None
    * `SINGLE`None
    '''
    __schema__ = model
    __choices__ = ('MULTIPLE', 'SINGLE')


class RelationshipTypeFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CHILDREN`None
    * `OTHERS`None
    * `PARENTS`None
    * `UNRELATED`None
    '''
    __schema__ = model
    __choices__ = ('CHILDREN', 'OTHERS', 'PARENTS', 'UNRELATED')


class ResultID(sgqlc.types.Scalar):
    __schema__ = model


class ReviewsSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HELPFULNESS_SCORE`None
    * `SUBMISSION_DATE`None
    * `SUBMITTER_REVIEW_COUNT`None
    * `TOTAL_VOTES`None
    * `USER_RATING`None
    '''
    __schema__ = model
    __choices__ = ('HELPFULNESS_SCORE', 'SUBMISSION_DATE', 'SUBMITTER_REVIEW_COUNT', 'TOTAL_VOTES', 'USER_RATING')


class SearchTheaterAttribute(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ONLINE_TICKETING`None
    '''
    __schema__ = model
    __choices__ = ('ONLINE_TICKETING',)


class SearchWatchOptionType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ANY_DIGITAL`None
    * `SUBSCRIPTION`None
    '''
    __schema__ = model
    __choices__ = ('ANY_DIGITAL', 'SUBSCRIPTION')


class SeverityVote(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MILD`None
    * `MODERATE`None
    * `NONE`None
    * `SEVERE`None
    '''
    __schema__ = model
    __choices__ = ('MILD', 'MODERATE', 'NONE', 'SEVERE')


class ShowtimesTitlesSortField(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `SHOWTIMES_COUNT`None
    '''
    __schema__ = model
    __choices__ = ('SHOWTIMES_COUNT',)


class ShowtimesTitlesSortOrder(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ASC`None
    * `DESC`None
    '''
    __schema__ = model
    __choices__ = ('ASC', 'DESC')


class SingleUserRatingSearchFilterType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE`None
    * `INCLUDE`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE', 'INCLUDE')


class SortOrder(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ASC`None
    * `DESC`None
    '''
    __schema__ = model
    __choices__ = ('ASC', 'DESC')


class SortSearchOrder(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ASC`None
    * `DESC`None
    '''
    __schema__ = model
    __choices__ = ('ASC', 'DESC')


class StaffCategory(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `IMDb`None
    '''
    __schema__ = model
    __choices__ = ('IMDb',)


String = sgqlc.types.String

class SuggestionSearchType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `INTEREST`None
    * `NAME`None
    * `TITLE`None
    '''
    __schema__ = model
    __choices__ = ('INTEREST', 'NAME', 'TITLE')


class TicketingType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ONLINE`None
    '''
    __schema__ = model
    __choices__ = ('ONLINE',)


class TimeUnit(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `SECONDS`None
    '''
    __schema__ = model
    __choices__ = ('SECONDS',)


class TitleChartRankingsType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BOTTOM_100`None
    * `TOP_250`None
    * `TOP_250_ENGLISH`None
    * `TOP_250_INDIA`None
    * `TOP_250_TV`None
    * `TOP_50_BENGALI`None
    * `TOP_50_MALAYALAM`None
    * `TOP_50_TAMIL`None
    * `TOP_50_TELUGU`None
    '''
    __schema__ = model
    __choices__ = ('BOTTOM_100', 'TOP_250', 'TOP_250_ENGLISH', 'TOP_250_INDIA', 'TOP_250_TV', 'TOP_50_BENGALI', 'TOP_50_MALAYALAM', 'TOP_50_TAMIL', 'TOP_50_TELUGU')


class TitleCreditSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `TOP_CAST`None
    '''
    __schema__ = model
    __choices__ = ('TOP_CAST',)


class TitleDataType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALTERNATE_VERSION`None
    * `AWARD`None
    * `BUSINESS_INFO`None
    * `CRAZY_CREDIT`None
    * `GOOF`None
    * `LOCATION`None
    * `PLOT`None
    * `QUOTE`None
    * `SOUNDTRACK`None
    * `TECHNICAL`None
    * `TRIVIA`None
    '''
    __schema__ = model
    __choices__ = ('ALTERNATE_VERSION', 'AWARD', 'BUSINESS_INFO', 'CRAZY_CREDIT', 'GOOF', 'LOCATION', 'PLOT', 'QUOTE', 'SOUNDTRACK', 'TECHNICAL', 'TRIVIA')


class TitleFacetField(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `GENRES`None
    * `KEYWORDS`None
    * `NAME_JOB_CATEGORIES`None
    * `TITLE_TYPE`None
    * `WATCH_PROVIDERS`None
    '''
    __schema__ = model
    __choices__ = ('GENRES', 'KEYWORDS', 'NAME_JOB_CATEGORIES', 'TITLE_TYPE', 'WATCH_PROVIDERS')


class TitleKeywordsSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALPHABETICAL`None
    '''
    __schema__ = model
    __choices__ = ('ALPHABETICAL',)


class TitleListSearchSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BOX_OFFICE_GROSS_DOMESTIC`None
    * `DATE_ADDED`None
    * `LIST_ORDER`None
    * `METACRITIC_SCORE`None
    * `MY_RATING`None
    * `MY_RATING_DATE`None
    * `POPULARITY`None
    * `RANKING`None
    * `RELEASE_DATE`None
    * `RUNTIME`None
    * `SINGLE_USER_RATING`None
    * `SINGLE_USER_RATING_DATE`None
    * `TITLE_REGIONAL`None
    * `USER_RATING`None
    * `USER_RATING_COUNT`None
    * `YEAR`None
    '''
    __schema__ = model
    __choices__ = ('BOX_OFFICE_GROSS_DOMESTIC', 'DATE_ADDED', 'LIST_ORDER', 'METACRITIC_SCORE', 'MY_RATING', 'MY_RATING_DATE', 'POPULARITY', 'RANKING', 'RELEASE_DATE', 'RUNTIME', 'SINGLE_USER_RATING', 'SINGLE_USER_RATING_DATE', 'TITLE_REGIONAL', 'USER_RATING', 'USER_RATING_COUNT', 'YEAR')


class TitleMeterType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `MOVIE_METER`None
    * `TITLE_METER`None
    * `TV_METER`None
    '''
    __schema__ = model
    __choices__ = ('MOVIE_METER', 'TITLE_METER', 'TV_METER')


class TitleTypeCategoryValue(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `audio`None
    * `gaming`None
    * `movie`None
    * `music`None
    * `other`None
    * `tv`None
    * `video`None
    '''
    __schema__ = model
    __choices__ = ('audio', 'gaming', 'movie', 'music', 'other', 'tv', 'video')


class TopGrossingReleasesTimeWindowPeriod(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `LATEST_DAY`None
    * `LATEST_WEEKEND`None
    '''
    __schema__ = model
    __choices__ = ('LATEST_DAY', 'LATEST_WEEKEND')


class TopListType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL`None
    * `EDITORIAL`None
    '''
    __schema__ = model
    __choices__ = ('ALL', 'EDITORIAL')


class TopMeterTitlesType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL`None
    * `MOVIE`None
    * `TV`None
    '''
    __schema__ = model
    __choices__ = ('ALL', 'MOVIE', 'TV')


class TopTrendingPredefinedEnum(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `INDIA_TITLE_TRENDS_RELEASED`None
    * `INDIA_TITLE_TRENDS_RELEASED_TAMIL`None
    * `INDIA_TITLE_TRENDS_RELEASED_TELUGU`None
    * `INDIA_TITLE_TRENDS_UPCOMING`None
    '''
    __schema__ = model
    __choices__ = ('INDIA_TITLE_TRENDS_RELEASED', 'INDIA_TITLE_TRENDS_RELEASED_TAMIL', 'INDIA_TITLE_TRENDS_RELEASED_TELUGU', 'INDIA_TITLE_TRENDS_UPCOMING')


class TrendingDataWindow(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HOURS`None
    * `MINUTES`None
    '''
    __schema__ = model
    __choices__ = ('HOURS', 'MINUTES')


class TrendingTrafficSource(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `XWW`None
    '''
    __schema__ = model
    __choices__ = ('XWW',)


class URL(sgqlc.types.Scalar):
    __schema__ = model


class UnknownReleaseDateFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_UNKNOWN`None
    * `UNKNOWN_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_UNKNOWN', 'UNKNOWN_ONLY')


class UserCategory(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `IMDB_USERS`None
    * `TOP_1000_VOTERS`None
    '''
    __schema__ = model
    __choices__ = ('IMDB_USERS', 'TOP_1000_VOTERS')


class UserReviewsSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `SUBMISSION_DATE`None
    '''
    __schema__ = model
    __choices__ = ('SUBMISSION_DATE',)


class UserRole(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ADMIN`None
    * `CUSTOMER`None
    '''
    __schema__ = model
    __choices__ = ('ADMIN', 'CUSTOMER')


class VideoAppearance(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HORIZONTAL`None
    * `SQUARE`None
    * `VERTICAL`None
    '''
    __schema__ = model
    __choices__ = ('HORIZONTAL', 'SQUARE', 'VERTICAL')


class VideoContentTypeId(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CLIP`None
    * `DEMO_REEL`None
    * `FEATURETTE`None
    * `FEATURE_FILM`None
    * `FILM_SHORT`None
    * `INTERVIEW`None
    * `MUSIC_VIDEO`None
    * `NEWS`None
    * `OTHER`None
    * `PROMOTIONAL`None
    * `REVIEW`None
    * `TRAILER`None
    * `TV_MINISODE`None
    * `TV_PROGRAM`None
    * `WEB_CLIP`None
    '''
    __schema__ = model
    __choices__ = ('CLIP', 'DEMO_REEL', 'FEATURETTE', 'FEATURE_FILM', 'FILM_SHORT', 'INTERVIEW', 'MUSIC_VIDEO', 'NEWS', 'OTHER', 'PROMOTIONAL', 'REVIEW', 'TRAILER', 'TV_MINISODE', 'TV_PROGRAM', 'WEB_CLIP')


class VideoDefinition(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DEF_1080p`None
    * `DEF_240p`None
    * `DEF_360p`None
    * `DEF_480p`None
    * `DEF_720p`None
    * `DEF_AUTO`None
    * `DEF_SD`None
    '''
    __schema__ = model
    __choices__ = ('DEF_1080p', 'DEF_240p', 'DEF_360p', 'DEF_480p', 'DEF_720p', 'DEF_AUTO', 'DEF_SD')


class VideoMimeType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `M3U8`None
    * `MP4`None
    * `WEBM`None
    '''
    __schema__ = model
    __choices__ = ('M3U8', 'MP4', 'WEBM')


class VideoPlacementType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `POSTROLL`None
    * `PREROLL`None
    '''
    __schema__ = model
    __choices__ = ('POSTROLL', 'PREROLL')


class VideoRecommendationsAdType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DISPLAY_AD`None
    '''
    __schema__ = model
    __choices__ = ('DISPLAY_AD',)


class VideoRecommendationsDisplayType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `PORTRAIT_ORIENTATION`None
    '''
    __schema__ = model
    __choices__ = ('PORTRAIT_ORIENTATION',)


class VideoSortBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DATE`None
    * `DURATION`None
    '''
    __schema__ = model
    __choices__ = ('DATE', 'DURATION')


class VideoTimedTextTrackFormat(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `SRT`None
    '''
    __schema__ = model
    __choices__ = ('SRT',)


class VideoTimedTextTrackType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CLOSED_CAPTION`None
    * `SUBTITLE`None
    '''
    __schema__ = model
    __choices__ = ('CLOSED_CAPTION', 'SUBTITLE')


class VisibilityLevel(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HIDDEN`None
    * `PRO_SITE_ONLY`None
    * `PUBLIC`None
    '''
    __schema__ = model
    __choices__ = ('HIDDEN', 'PRO_SITE_ONLY', 'PUBLIC')


class WatchOptionCategoryType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `IMDB_TV`None
    * `PHYSICAL`None
    * `PODCAST`None
    * `RENT_OR_BUY`None
    * `SUBSCRIPTION`None
    * `THEATRICAL`None
    '''
    __schema__ = model
    __choices__ = ('IMDB_TV', 'PHYSICAL', 'PODCAST', 'RENT_OR_BUY', 'SUBSCRIPTION', 'THEATRICAL')


class WeightUnit(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `KILOGRAM`None
    * `POUND`None
    '''
    __schema__ = model
    __choices__ = ('KILOGRAM', 'POUND')


class WideReleaseFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_WIDE_RELEASE`None
    * `WIDE_RELEASE_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_WIDE_RELEASE', 'WIDE_RELEASE_ONLY')


class WinsFilter(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXCLUDE_WINS`None
    * `WINS_ONLY`None
    '''
    __schema__ = model
    __choices__ = ('EXCLUDE_WINS', 'WINS_ONLY')



########################################################################
# Input Objects
########################################################################
class AdParametersApp(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('auto_start_video', 'context', 'device_id', 'device_info', 'idfa', 'page_type', 'sub_page_type', 'user_agent', 'viewport_size')
    auto_start_video = sgqlc.types.Field(Boolean, graphql_name='autoStartVideo')

    context = sgqlc.types.Field(String, graphql_name='context')

    device_id = sgqlc.types.Field(String, graphql_name='deviceId')

    device_info = sgqlc.types.Field(sgqlc.types.non_null('DeviceInfo'), graphql_name='deviceInfo')

    idfa = sgqlc.types.Field(String, graphql_name='idfa')

    page_type = sgqlc.types.Field(String, graphql_name='pageType')

    sub_page_type = sgqlc.types.Field(String, graphql_name='subPageType')

    user_agent = sgqlc.types.Field(String, graphql_name='userAgent')

    viewport_size = sgqlc.types.Field('ViewPortSize', graphql_name='viewportSize')



class AdParametersWeb(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('auto_start_video', 'context', 'page_type', 'sub_page_type', 'user_agent', 'viewport_size')
    auto_start_video = sgqlc.types.Field(Boolean, graphql_name='autoStartVideo')

    context = sgqlc.types.Field(String, graphql_name='context')

    page_type = sgqlc.types.Field(String, graphql_name='pageType')

    sub_page_type = sgqlc.types.Field(String, graphql_name='subPageType')

    user_agent = sgqlc.types.Field(String, graphql_name='userAgent')

    viewport_size = sgqlc.types.Field('ViewPortSize', graphql_name='viewportSize')



class AdvancedNameSearchConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('award_constraint', 'biography_constraint', 'birth_date_constraint', 'birth_place_constraint', 'death_date_constraint', 'death_place_constraint', 'explicit_content_constraint', 'filmography_constraint', 'gender_identity_constraint', 'list_constraint', 'name_text_constraint', 'quote_matching_constraint', 'trivia_matching_constraint', 'with_name_data_constraint')
    award_constraint = sgqlc.types.Field('AwardSearchConstraint', graphql_name='awardConstraint')

    biography_constraint = sgqlc.types.Field('BiographySearchConstraint', graphql_name='biographyConstraint')

    birth_date_constraint = sgqlc.types.Field('BirthDateSearchConstraint', graphql_name='birthDateConstraint')

    birth_place_constraint = sgqlc.types.Field('BirthPlaceSearchConstraint', graphql_name='birthPlaceConstraint')

    death_date_constraint = sgqlc.types.Field('DeathDateSearchConstraint', graphql_name='deathDateConstraint')

    death_place_constraint = sgqlc.types.Field('DeathPlaceSearchConstraint', graphql_name='deathPlaceConstraint')

    explicit_content_constraint = sgqlc.types.Field('ExplicitContentSearchConstraint', graphql_name='explicitContentConstraint')

    filmography_constraint = sgqlc.types.Field('FilmographySearchConstraint', graphql_name='filmographyConstraint')

    gender_identity_constraint = sgqlc.types.Field('GenderIdentitySearchConstraint', graphql_name='genderIdentityConstraint')

    list_constraint = sgqlc.types.Field('ListSearchConstraint', graphql_name='listConstraint')

    name_text_constraint = sgqlc.types.Field('NameTextSearchConstraint', graphql_name='nameTextConstraint')

    quote_matching_constraint = sgqlc.types.Field('NameQuoteMatchingSearchConstraint', graphql_name='quoteMatchingConstraint')

    trivia_matching_constraint = sgqlc.types.Field('NameTriviaMatchingSearchConstraint', graphql_name='triviaMatchingConstraint')

    with_name_data_constraint = sgqlc.types.Field('WithNameDataSearchConstraint', graphql_name='withNameDataConstraint')



class AdvancedNameSearchSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('sort_by', 'sort_order')
    sort_by = sgqlc.types.Field(sgqlc.types.non_null(AdvancedNameSearchSortBy), graphql_name='sortBy')

    sort_order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='sortOrder')



class AdvancedTitleSearchConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('alternate_version_matching_constraint', 'award_constraint', 'certificate_constraint', 'character_constraint', 'coloration_constraint', 'crazy_credit_matching_constraint', 'credited_company_constraint', 'credited_name_constraint', 'current_production_status_stage_constraint', 'episodic_constraint', 'explicit_content_constraint', 'filming_location_constraint', 'genre_constraint', 'goof_matching_constraint', 'in_theaters_constraint', 'interest_constraint', 'keyword_constraint', 'language_constraint', 'list_constraint', 'my_rating_constraint', 'origin_country_constraint', 'plot_matching_constraint', 'quote_matching_constraint', 'ranked_title_list_constraint', 'release_date_constraint', 'runtime_constraint', 'single_user_rating_constraint', 'sound_mix_constraint', 'soundtrack_matching_constraint', 'title_credits_constraint', 'title_meter_constraint', 'title_text_constraint', 'title_type_constraint', 'trivia_matching_constraint', 'user_ratings_constraint', 'watch_options_constraint', 'with_title_data_constraint')
    alternate_version_matching_constraint = sgqlc.types.Field('AlternateVersionMatchingSearchConstraint', graphql_name='alternateVersionMatchingConstraint')

    award_constraint = sgqlc.types.Field('AwardSearchConstraint', graphql_name='awardConstraint')

    certificate_constraint = sgqlc.types.Field('CertificateSearchConstraint', graphql_name='certificateConstraint')

    character_constraint = sgqlc.types.Field('CharacterSearchConstraint', graphql_name='characterConstraint')

    coloration_constraint = sgqlc.types.Field('ColorationSearchConstraint', graphql_name='colorationConstraint')

    crazy_credit_matching_constraint = sgqlc.types.Field('CrazyCreditMatchingSearchConstraint', graphql_name='crazyCreditMatchingConstraint')

    credited_company_constraint = sgqlc.types.Field('CreditedCompanySearchConstraint', graphql_name='creditedCompanyConstraint')

    credited_name_constraint = sgqlc.types.Field('CreditedNameConstraint', graphql_name='creditedNameConstraint')

    current_production_status_stage_constraint = sgqlc.types.Field('CurrentProductionStatusStageConstraint', graphql_name='currentProductionStatusStageConstraint')

    episodic_constraint = sgqlc.types.Field('EpisodicSearchConstraint', graphql_name='episodicConstraint')

    explicit_content_constraint = sgqlc.types.Field('ExplicitContentSearchConstraint', graphql_name='explicitContentConstraint')

    filming_location_constraint = sgqlc.types.Field('FilmingLocationSearchConstraint', graphql_name='filmingLocationConstraint')

    genre_constraint = sgqlc.types.Field('GenreSearchConstraint', graphql_name='genreConstraint')

    goof_matching_constraint = sgqlc.types.Field('GoofMatchingSearchConstraint', graphql_name='goofMatchingConstraint')

    in_theaters_constraint = sgqlc.types.Field('InTheatersSearchConstraint', graphql_name='inTheatersConstraint')

    interest_constraint = sgqlc.types.Field('InterestSearchConstraint', graphql_name='interestConstraint')

    keyword_constraint = sgqlc.types.Field('KeywordSearchConstraint', graphql_name='keywordConstraint')

    language_constraint = sgqlc.types.Field('LanguageSearchConstraint', graphql_name='languageConstraint')

    list_constraint = sgqlc.types.Field('ListSearchConstraint', graphql_name='listConstraint')

    my_rating_constraint = sgqlc.types.Field('MyRatingSearchConstraint', graphql_name='myRatingConstraint')

    origin_country_constraint = sgqlc.types.Field('OriginCountrySearchConstraint', graphql_name='originCountryConstraint')

    plot_matching_constraint = sgqlc.types.Field('PlotMatchingSearchConstraint', graphql_name='plotMatchingConstraint')

    quote_matching_constraint = sgqlc.types.Field('TitleQuoteMatchingSearchConstraint', graphql_name='quoteMatchingConstraint')

    ranked_title_list_constraint = sgqlc.types.Field('RankedTitleListSearchConstraint', graphql_name='rankedTitleListConstraint')

    release_date_constraint = sgqlc.types.Field('ReleaseDateSearchConstraint', graphql_name='releaseDateConstraint')

    runtime_constraint = sgqlc.types.Field('RuntimeSearchConstraint', graphql_name='runtimeConstraint')

    single_user_rating_constraint = sgqlc.types.Field('SingleUserRatingSearchConstraint', graphql_name='singleUserRatingConstraint')

    sound_mix_constraint = sgqlc.types.Field('SoundMixSearchConstraint', graphql_name='soundMixConstraint')

    soundtrack_matching_constraint = sgqlc.types.Field('SoundtrackMatchingSearchConstraint', graphql_name='soundtrackMatchingConstraint')

    title_credits_constraint = sgqlc.types.Field('TitleCreditsConstraint', graphql_name='titleCreditsConstraint')

    title_meter_constraint = sgqlc.types.Field('TitleMeterSearchConstraint', graphql_name='titleMeterConstraint')

    title_text_constraint = sgqlc.types.Field('TitleTextSearchConstraint', graphql_name='titleTextConstraint')

    title_type_constraint = sgqlc.types.Field('TitleTypeSearchConstraint', graphql_name='titleTypeConstraint')

    trivia_matching_constraint = sgqlc.types.Field('TitleTriviaMatchingSearchConstraint', graphql_name='triviaMatchingConstraint')

    user_ratings_constraint = sgqlc.types.Field('UserRatingsSearchConstraint', graphql_name='userRatingsConstraint')

    watch_options_constraint = sgqlc.types.Field('WatchOptionsSearchConstraint', graphql_name='watchOptionsConstraint')

    with_title_data_constraint = sgqlc.types.Field('WithTitleDataSearchConstraint', graphql_name='withTitleDataConstraint')



class AdvancedTitleSearchSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('sort_by', 'sort_order')
    sort_by = sgqlc.types.Field(sgqlc.types.non_null(AdvancedTitleSearchSortBy), graphql_name='sortBy')

    sort_order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='sortOrder')



class AkaSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(AkaSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class AlternateVersionMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_alternate_version_text_terms', 'any_alternate_version_text_terms')
    all_alternate_version_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allAlternateVersionTextTerms')

    any_alternate_version_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyAlternateVersionTextTerms')



class AttachmentSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('attachment_group',)
    attachment_group = sgqlc.types.Field(sgqlc.types.non_null(AttachmentGroup), graphql_name='attachmentGroup')



class AwardEventNominationSearchInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('event_id', 'search_award_category_id', 'winner_filter')
    event_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='eventId')

    search_award_category_id = sgqlc.types.Field(ID, graphql_name='searchAwardCategoryId')

    winner_filter = sgqlc.types.Field(AwardWinnerSearchFilter, graphql_name='winnerFilter')



class AwardNominationsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('awards', 'events', 'wins')
    awards = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='awards')

    events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='events')

    wins = sgqlc.types.Field(WinsFilter, graphql_name='wins')



class AwardNominationsSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(AwardNominationsSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class AwardSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_event_nominations', 'any_event_nominations', 'exclude_event_nominations')
    all_event_nominations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AwardEventNominationSearchInput)), graphql_name='allEventNominations')

    any_event_nominations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AwardEventNominationSearchInput)), graphql_name='anyEventNominations')

    exclude_event_nominations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AwardEventNominationSearchInput)), graphql_name='excludeEventNominations')



class AwardsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_awards', 'include_awards')
    exclude_awards = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeAwards')

    include_awards = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeAwards')



class BiographySearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_biography_authors', 'search_text')
    any_biography_authors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyBiographyAuthors')

    search_text = sgqlc.types.Field(String, graphql_name='searchText')



class BirthDateSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('birth_date_range', 'birthday')
    birth_date_range = sgqlc.types.Field('DateRange', graphql_name='birthDateRange')

    birthday = sgqlc.types.Field(MonthDay, graphql_name='birthday')



class BirthPlaceSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('birth_place',)
    birth_place = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='birthPlace')



class BoxOfficeReleasesAreaFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('box_office_area', 'country')
    box_office_area = sgqlc.types.Field(String, graphql_name='boxOfficeArea')

    country = sgqlc.types.Field(String, graphql_name='country')



class CallToActionContextInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('const_id', 'is_logged_in')
    const_id = sgqlc.types.Field(ID, graphql_name='constId')

    is_logged_in = sgqlc.types.Field(Boolean, graphql_name='isLoggedIn')



class CertificateSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_region_certificate_ratings', 'exclude_region_certificate_ratings')
    any_region_certificate_ratings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RegionCertificateRatingInput')), graphql_name='anyRegionCertificateRatings')

    exclude_region_certificate_ratings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RegionCertificateRatingInput')), graphql_name='excludeRegionCertificateRatings')



class CertificatesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_countries', 'include_countries', 'ratings_body')
    exclude_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCountries')

    include_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeCountries')

    ratings_body = sgqlc.types.Field(ID, graphql_name='ratingsBody')



class CharacterSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_character_names', 'should_limit_to_credited_name_ids')
    any_character_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyCharacterNames')

    should_limit_to_credited_name_ids = sgqlc.types.Field(Boolean, graphql_name='shouldLimitToCreditedNameIds')



class ChartNameOptions(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('chart_type',)
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartNameType), graphql_name='chartType')



class ChartTitleOptions(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('chart_type',)
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartTitleType), graphql_name='chartType')



class ColorationSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_coloration_types', 'exclude_coloration_types')
    any_coloration_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ColorationType)), graphql_name='anyColorationTypes')

    exclude_coloration_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ColorationType)), graphql_name='excludeColorationTypes')



class ComingSoonSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('sort_by', 'sort_order')
    sort_by = sgqlc.types.Field(sgqlc.types.non_null(ComingSoonSortBy), graphql_name='sortBy')

    sort_order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='sortOrder')



class CompanyCreditsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories',)
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')



class CompanyImagesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('types',)
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='types')



class CompanyMeterRankingHistoryInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('end_date', 'start_date')
    end_date = sgqlc.types.Field(Date, graphql_name='endDate')

    start_date = sgqlc.types.Field(Date, graphql_name='startDate')



class ConnectionsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories',)
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')



class ContributionContext(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('business', 'is_in_iframe', 'return_url')
    business = sgqlc.types.Field(String, graphql_name='business')

    is_in_iframe = sgqlc.types.Field(Boolean, graphql_name='isInIframe')

    return_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='returnUrl')



class ContributorLeaderboardRankingsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('maximum_rank',)
    maximum_rank = sgqlc.types.Field(Int, graphql_name='maximumRank')



class ContributorLeaderboardsByMonthFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('months', 'years')
    months = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='months')

    years = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='years')



class ContributorLeaderboardsByYearFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('years',)
    years = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='years')



class ContributorRankSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(ContributorRankSortBy, graphql_name='by')

    order = sgqlc.types.Field(SortOrder, graphql_name='order')



class ContributorRankingsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('contributor_id', 'months', 'period', 'years')
    contributor_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='contributorId')

    months = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='months')

    period = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ContributorLeaderboardPeriodTypeId)), graphql_name='period')

    years = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='years')



class CountInterval(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('max', 'min')
    max = sgqlc.types.Field(Int, graphql_name='max')

    min = sgqlc.types.Field(Int, graphql_name='min')



class CrazyCreditMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_crazy_credit_text_terms', 'any_crazy_credit_text_terms')
    all_crazy_credit_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allCrazyCreditTextTerms')

    any_crazy_credit_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyCrazyCreditTextTerms')



class CreditedCompanySearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_company_ids', 'any_company_categories', 'any_company_ids', 'exclude_company_ids')
    all_company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allCompanyIds')

    any_company_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyCompanyCategories')

    any_company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyCompanyIds')

    exclude_company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCompanyIds')



class CreditedNameConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_name_ids', 'any_name_ids', 'exclude_name_ids')
    all_name_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allNameIds')

    any_name_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyNameIds')

    exclude_name_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeNameIds')



class CreditsCompletenessStatusFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_values',)
    exclude_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeValues')



class CurrentProductionStatusStageConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_production_stage_ids', 'exclude_production_stage_ids')
    any_production_stage_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyProductionStageIds')

    exclude_production_stage_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeProductionStageIds')



class DateRange(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(Date, graphql_name='end')

    start = sgqlc.types.Field(Date, graphql_name='start')



class DeathDateSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('death_date_range',)
    death_date_range = sgqlc.types.Field(sgqlc.types.non_null(DateRange), graphql_name='deathDateRange')



class DeathPlaceSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('death_place',)
    death_place = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deathPlace')



class DemographicDataFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_types', 'include_types', 'self_verified', 'visibility')
    exclude_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DemographicDataTypeValue)), graphql_name='excludeTypes')

    include_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DemographicDataTypeValue)), graphql_name='includeTypes')

    self_verified = sgqlc.types.Field(Boolean, graphql_name='selfVerified')

    visibility = sgqlc.types.Field(VisibilityLevel, graphql_name='visibility')



class DemographicFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('age', 'country', 'gender', 'user_category')
    age = sgqlc.types.Field(Age, graphql_name='age')

    country = sgqlc.types.Field(Country, graphql_name='country')

    gender = sgqlc.types.Field(Gender, graphql_name='gender')

    user_category = sgqlc.types.Field(UserCategory, graphql_name='userCategory')



class DeviceInfo(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('carrier', 'make', 'model', 'os', 'os_version', 'scaling_factor')
    carrier = sgqlc.types.Field(String, graphql_name='carrier')

    make = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='make')

    model = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='model')

    os = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='os')

    os_version = sgqlc.types.Field(String, graphql_name='osVersion')

    scaling_factor = sgqlc.types.Field(String, graphql_name='scalingFactor')



class DisplayAdTargetingParameters(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('ad_layout', 'page_const', 'sub_section_type')
    ad_layout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='adLayout')

    page_const = sgqlc.types.Field(ID, graphql_name='pageConst')

    sub_section_type = sgqlc.types.Field(String, graphql_name='subSectionType')



class DisplayAdsForAppInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('ad_parameters_app', 'display_ad_targeting_parameters')
    ad_parameters_app = sgqlc.types.Field(sgqlc.types.non_null(AdParametersApp), graphql_name='adParametersApp')

    display_ad_targeting_parameters = sgqlc.types.Field(sgqlc.types.non_null(DisplayAdTargetingParameters), graphql_name='displayAdTargetingParameters')



class EpisodeReleaseDate(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('day', 'month', 'year')
    day = sgqlc.types.Field(Int, graphql_name='day')

    month = sgqlc.types.Field(Int, graphql_name='month')

    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')



class EpisodesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_seasons', 'include_seasons', 'released_on_or_after', 'released_on_or_before', 'unknown_release_date')
    exclude_seasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeSeasons')

    include_seasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='includeSeasons')

    released_on_or_after = sgqlc.types.Field(EpisodeReleaseDate, graphql_name='releasedOnOrAfter')

    released_on_or_before = sgqlc.types.Field(EpisodeReleaseDate, graphql_name='releasedOnOrBefore')

    unknown_release_date = sgqlc.types.Field(UnknownReleaseDateFilter, graphql_name='unknownReleaseDate')



class EpisodesSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(EpisodesSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class EpisodicSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_episode_numbers', 'any_seasons', 'any_series_ids', 'exclude_episode_numbers', 'exclude_seasons', 'exclude_series_ids')
    any_episode_numbers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyEpisodeNumbers')

    any_seasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anySeasons')

    any_series_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anySeriesIds')

    exclude_episode_numbers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeEpisodeNumbers')

    exclude_seasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeSeasons')

    exclude_series_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeSeriesIds')



class EventLiveResultsOverrideInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('enable_override', 'override_event')
    enable_override = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableOverride')

    override_event = sgqlc.types.Field('OverrideLiveEventInput', graphql_name='overrideEvent')



class EventsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_events', 'include_events')
    exclude_events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeEvents')

    include_events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeEvents')



class ExperimentalTitleCreditsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'copy_jobs', 'credited', 'exclude_categories', 'exclude_principal', 'names')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    copy_jobs = sgqlc.types.Field(Boolean, graphql_name='copy_jobs')

    credited = sgqlc.types.Field(CreditedOrUncreditedFilter, graphql_name='credited')

    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')

    exclude_principal = sgqlc.types.Field(Boolean, graphql_name='excludePrincipal')

    names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='names')



class Experimental_AdditionalCreditCategoriesInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_categories', 'include_categories')
    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')

    include_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeCategories')



class Experimental_AdditionalCreditsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_categories',)
    include_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeCategories')



class Experimental_CatalogQueryInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('title_id',)
    title_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='titleId')



class Experimental_GetLatestUIWorkflowInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('execution_id',)
    execution_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='executionId')



class Experimental_UploadDestinationInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('count', 'type')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')

    type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UploadMediaType), graphql_name='type')



class ExplicitContentSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('explicit_content_filter',)
    explicit_content_filter = sgqlc.types.Field(ExplicitContentFilter, graphql_name='explicitContentFilter')



class ExportFilterByInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('status',)
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExportStatusId)), graphql_name='status')



class ExportSortByInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(ExportSortByField), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class ExternalLinksFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'exclude_categories')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')



class FanPicksFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_title_types',)
    include_title_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleTypeCategoryValue)), graphql_name='includeTitleTypes')



class FaqsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('has_answer', 'spoilers')
    has_answer = sgqlc.types.Field(Boolean, graphql_name='hasAnswer')

    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class FeedbackGivenInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('feature_type',)
    feature_type = sgqlc.types.Field(sgqlc.types.non_null(FeedbackGivenFeatureType), graphql_name='featureType')



class FilmingLocationSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_locations', 'any_locations')
    all_locations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allLocations')

    any_locations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyLocations')



class FilmographySearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_title_ids', 'any_title_ids', 'exclude_title_ids')
    all_title_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allTitleIds')

    any_title_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyTitleIds')

    exclude_title_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeTitleIds')



class FilterPlots(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('spoilers', 'type')
    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')

    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PlotType)), graphql_name='type')



class FloatRangeInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('max', 'min')
    max = sgqlc.types.Field(Float, graphql_name='max')

    min = sgqlc.types.Field(Float, graphql_name='min')



class GenderIdentitySearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_gender', 'exclude_gender')
    any_gender = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameGenderIdentity)), graphql_name='anyGender')

    exclude_gender = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameGenderIdentity)), graphql_name='excludeGender')



class GenreSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_genre_ids', 'any_genre_ids', 'exclude_genre_ids', 'max_relevant_genres')
    all_genre_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allGenreIds')

    any_genre_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyGenreIds')

    exclude_genre_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeGenreIds')

    max_relevant_genres = sgqlc.types.Field(Int, graphql_name='maxRelevantGenres')



class GenreSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(GenreSortBy, graphql_name='by')

    order = sgqlc.types.Field(SortOrder, graphql_name='order')



class GetExportsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('export_types',)
    export_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExportType))), graphql_name='exportTypes')



class GetNameWeightInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('unit',)
    unit = sgqlc.types.Field(WeightUnit, graphql_name='unit')



class GetPlacementsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('additional_page_targeting_criteria', 'container_id', 'container_type', 'query_params', 'slot_names')
    additional_page_targeting_criteria = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SymphonyMultiValueMapEntry')), graphql_name='additionalPageTargetingCriteria')

    container_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='containerId')

    container_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='containerType')

    query_params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SymphonyMultiValueMapEntry')), graphql_name='queryParams')

    slot_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='slotNames')



class GoofCategoryWithGoofsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('spoilers',)
    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class GoofMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_goof_text_terms', 'any_goof_text_terms')
    all_goof_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allGoofTextTerms')

    any_goof_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyGoofTextTerms')



class GoofsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'exclude_categories', 'spoilers')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')

    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class GuildAffiliationsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_data_verification_types',)
    include_data_verification_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GuildDataVerificationType)), graphql_name='includeDataVerificationTypes')



class ImageGalleryFilterConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_gallery_ids', 'any_gallery_ids')
    all_gallery_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allGalleryIds')

    any_gallery_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyGalleryIds')



class ImageNameFilterConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_name_ids', 'any_name_ids')
    all_name_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allNameIds')

    any_name_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyNameIds')



class ImageTitleFilterConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_title_ids', 'any_title_ids')
    all_title_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allTitleIds')

    any_title_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyTitleIds')



class ImagesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('gallery_constraints', 'name_constraints', 'names_count', 'title_constraints', 'types')
    gallery_constraints = sgqlc.types.Field(ImageGalleryFilterConstraints, graphql_name='galleryConstraints')

    name_constraints = sgqlc.types.Field(ImageNameFilterConstraints, graphql_name='nameConstraints')

    names_count = sgqlc.types.Field(CountInterval, graphql_name='namesCount')

    title_constraints = sgqlc.types.Field(ImageTitleFilterConstraints, graphql_name='titleConstraints')

    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='types')



class InTheatersSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_theater_attributes', 'location', 'my_favorite_theaters')
    all_theater_attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SearchTheaterAttribute)), graphql_name='allTheaterAttributes')

    location = sgqlc.types.Field('ShowtimesLocation', graphql_name='location')

    my_favorite_theaters = sgqlc.types.Field(MyFavoriteTheaterSearchFilter, graphql_name='myFavoriteTheaters')



class IntRangeInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('max', 'min')
    max = sgqlc.types.Field(Int, graphql_name='max')

    min = sgqlc.types.Field(Int, graphql_name='min')



class InterestCategoriesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories',)
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')



class InterestSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_interest_ids', 'any_interest_ids', 'exclude_interest_ids')
    all_interest_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allInterestIds')

    any_interest_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyInterestIds')

    exclude_interest_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeInterestIds')



class KeywordSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_keywords', 'any_keywords', 'exclude_keywords')
    all_keywords = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allKeywords')

    any_keywords = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyKeywords')

    exclude_keywords = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeKeywords')



class LanguageSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_languages', 'any_languages', 'any_primary_languages', 'exclude_languages', 'exclude_primary_languages', 'is_silent')
    all_languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allLanguages')

    any_languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyLanguages')

    any_primary_languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyPrimaryLanguages')

    exclude_languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeLanguages')

    exclude_primary_languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludePrimaryLanguages')

    is_silent = sgqlc.types.Field(Boolean, graphql_name='isSilent')



class LatLong(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('lat', 'long')
    lat = sgqlc.types.Field(sgqlc.types.non_null(LocationDecimal), graphql_name='lat')

    long = sgqlc.types.Field(sgqlc.types.non_null(LocationDecimal), graphql_name='long')



class LatestTrailerFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('country', 'maturity_level', 'preferred_audio_language')
    country = sgqlc.types.Field(String, graphql_name='country')

    maturity_level = sgqlc.types.Field(MaturityLevel, graphql_name='maturityLevel')

    preferred_audio_language = sgqlc.types.Field(Language, graphql_name='preferredAudioLanguage')



class ListFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('class_types', 'list_element_type')
    class_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ListClassId)), graphql_name='classTypes')

    list_element_type = sgqlc.types.Field(ListTypeId, graphql_name='listElementType')



class ListItemFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('rated', 'released')
    rated = sgqlc.types.Field(FilterInclusion, graphql_name='rated')

    released = sgqlc.types.Field(FilterInclusion, graphql_name='released')



class ListItemSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(ListItemSortBy, graphql_name='by')

    order = sgqlc.types.Field(SortOrder, graphql_name='order')



class ListSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('in_all_lists', 'in_all_predefined_lists', 'in_any_list', 'in_any_predefined_list', 'not_in_any_list', 'not_in_any_predefined_list')
    in_all_lists = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='inAllLists')

    in_all_predefined_lists = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PredefinedListInput')), graphql_name='inAllPredefinedLists')

    in_any_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='inAnyList')

    in_any_predefined_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PredefinedListInput')), graphql_name='inAnyPredefinedList')

    not_in_any_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='notInAnyList')

    not_in_any_predefined_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PredefinedListInput')), graphql_name='notInAnyPredefinedList')



class ListSearchFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_class_types', 'any_list_types', 'any_visibilities')
    any_class_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ListClassId)), graphql_name='anyClassTypes')

    any_list_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ListTypeId)), graphql_name='anyListTypes')

    any_visibilities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ListVisibilityId)), graphql_name='anyVisibilities')



class ListSearchSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(ListSearchSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortSearchOrder), graphql_name='order')



class MainSearchOptions(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_adult', 'is_exact_match', 'search_term', 'title_search_options', 'type')
    include_adult = sgqlc.types.Field(Boolean, graphql_name='includeAdult')

    is_exact_match = sgqlc.types.Field(Boolean, graphql_name='isExactMatch')

    search_term = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchTerm')

    title_search_options = sgqlc.types.Field('TitleSearchOptions', graphql_name='titleSearchOptions')

    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MainSearchType)), graphql_name='type')



class MyRatingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('filter_type', 'rating_range')
    filter_type = sgqlc.types.Field(sgqlc.types.non_null(MyRatingSearchFilterType), graphql_name='filterType')

    rating_range = sgqlc.types.Field(IntRangeInput, graphql_name='ratingRange')



class NameBiosFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'include_all_locales')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    include_all_locales = sgqlc.types.Field(Boolean, graphql_name='includeAllLocales')



class NameChartRankingsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('rankings_chart_type',)
    rankings_chart_type = sgqlc.types.Field(NameChartRankingsType, graphql_name='rankingsChartType')



class NameCreditCategoryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('archived', 'categories', 'credited', 'exclude_categories', 'exclude_genres', 'exclude_production_stage', 'exclude_title_type', 'genres', 'production_stage', 'professions', 'project_status', 'title_type', 'title_type_category', 'titles')
    archived = sgqlc.types.Field(ArchivedOrUnarchivedFilter, graphql_name='archived')

    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    credited = sgqlc.types.Field(CreditedOrUncreditedFilter, graphql_name='credited')

    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')

    exclude_genres = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeGenres')

    exclude_production_stage = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionStageFilter)), graphql_name='excludeProductionStage')

    exclude_title_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeTitleType')

    genres = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='genres')

    production_stage = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionStageFilter)), graphql_name='productionStage')

    professions = sgqlc.types.Field(ProfessionsFilter, graphql_name='professions')

    project_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectStatus')

    title_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='titleType')

    title_type_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleTypeCategoryValue)), graphql_name='titleTypeCategory')

    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='titles')



class NameCreditSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(NameCreditSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class NameCreditsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('archived', 'categories', 'credited', 'exclude_categories', 'exclude_genres', 'exclude_production_stage', 'exclude_title_type', 'genres', 'production_stage', 'project_status', 'title_type', 'title_type_category', 'titles')
    archived = sgqlc.types.Field(ArchivedOrUnarchivedFilter, graphql_name='archived')

    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    credited = sgqlc.types.Field(CreditedOrUncreditedFilter, graphql_name='credited')

    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')

    exclude_genres = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeGenres')

    exclude_production_stage = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionStageFilter)), graphql_name='excludeProductionStage')

    exclude_title_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeTitleType')

    genres = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='genres')

    production_stage = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionStageFilter)), graphql_name='productionStage')

    project_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectStatus')

    title_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='titleType')

    title_type_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleTypeCategoryValue)), graphql_name='titleTypeCategory')

    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='titles')



class NameImagesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('featured', 'gallery_constraints', 'name_constraints', 'names_count', 'title_constraints', 'types')
    featured = sgqlc.types.Field(FeaturedImagesOption, graphql_name='featured')

    gallery_constraints = sgqlc.types.Field(ImageGalleryFilterConstraints, graphql_name='galleryConstraints')

    name_constraints = sgqlc.types.Field(ImageNameFilterConstraints, graphql_name='nameConstraints')

    names_count = sgqlc.types.Field(CountInterval, graphql_name='namesCount')

    title_constraints = sgqlc.types.Field(ImageTitleFilterConstraints, graphql_name='titleConstraints')

    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='types')



class NameListSearchSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(NameListSearchSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class NameMeterRankingHistoryInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('end_date', 'start_date')
    end_date = sgqlc.types.Field(Date, graphql_name='endDate')

    start_date = sgqlc.types.Field(Date, graphql_name='startDate')



class NameQuoteMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_quote_text_terms', 'any_quote_text_terms')
    all_quote_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allQuoteTextTerms')

    any_quote_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyQuoteTextTerms')



class NameRelationsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_relationship_types', 'relationship_types')
    exclude_relationship_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationshipTypeFilter)), graphql_name='excludeRelationshipTypes')

    relationship_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationshipTypeFilter)), graphql_name='relationshipTypes')



class NameTextSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('search_term',)
    search_term = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchTerm')



class NameTriviaMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_trivia_text_terms', 'any_trivia_text_terms')
    all_trivia_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allTriviaTextTerms')

    any_trivia_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyTriviaTextTerms')



class NominationsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('awards', 'events', 'wins')
    awards = sgqlc.types.Field(AwardsFilter, graphql_name='awards')

    events = sgqlc.types.Field(EventsFilter, graphql_name='events')

    wins = sgqlc.types.Field(WinsFilter, graphql_name='wins')



class NominationsSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(NominationsSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class OpeningWeekendBoxOfficeGrossFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('box_office_area_codes',)
    box_office_area_codes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='boxOfficeAreaCodes')



class OriginCountrySearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_countries', 'any_countries', 'any_primary_countries', 'exclude_countries', 'exclude_primary_countries')
    all_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allCountries')

    any_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyCountries')

    any_primary_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyPrimaryCountries')

    exclude_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeCountries')

    exclude_primary_countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludePrimaryCountries')



class OutstreamAdParametersApp(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('ad_parameters_app', 'override_placement_type')
    ad_parameters_app = sgqlc.types.Field(sgqlc.types.non_null(AdParametersApp), graphql_name='adParametersApp')

    override_placement_type = sgqlc.types.Field(VideoPlacementType, graphql_name='overridePlacementType')



class OverrideLiveEventInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('award_id', 'event_edition_id')
    award_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='awardId')

    event_edition_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='eventEditionId')



class ParentsGuideCategoryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('spoilers',)
    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class ParentsGuideFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'spoilers')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class PlacementContext(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('page_type',)
    page_type = sgqlc.types.Field(String, graphql_name='pageType')



class PlotMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_plot_text_terms', 'any_plot_authors', 'any_plot_text_terms')
    all_plot_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allPlotTextTerms')

    any_plot_authors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyPlotAuthors')

    any_plot_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyPlotTextTerms')



class PopularTitlesQueryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('filter_out_user_ratings', 'release_date_range')
    filter_out_user_ratings = sgqlc.types.Field(Boolean, graphql_name='filterOutUserRatings')

    release_date_range = sgqlc.types.Field(DateRange, graphql_name='releaseDateRange')



class PostalCodeLocation(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('country', 'postal_code')
    country = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='country')

    postal_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='postalCode')



class PredefinedListInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('class_id',)
    class_id = sgqlc.types.Field(sgqlc.types.non_null(ListClassId), graphql_name='classId')



class PrincipalCreditsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories',)
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')



class PrivacyPromptInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('type',)
    type = sgqlc.types.Field(sgqlc.types.non_null(PrivacyPromptType), graphql_name='type')



class PromotedVideoAdParameters(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('ad_override_creative_id', 'ad_parameters_app')
    ad_override_creative_id = sgqlc.types.Field(String, graphql_name='adOverrideCreativeId')

    ad_parameters_app = sgqlc.types.Field(AdParametersApp, graphql_name='adParametersApp')



class PublicityListingsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories',)
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')



class QuestionsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('country', 'data_type', 'data_types', 'language')
    country = sgqlc.types.Field(String, graphql_name='country')

    data_type = sgqlc.types.Field(String, graphql_name='dataType')

    data_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='dataTypes')

    language = sgqlc.types.Field(String, graphql_name='language')



class RankedLifetimeBoxOfficeGrossFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('box_office_area_codes',)
    box_office_area_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='boxOfficeAreaCodes')



class RankedTitleList(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('rank_range', 'ranked_title_list_type')
    rank_range = sgqlc.types.Field(IntRangeInput, graphql_name='rankRange')

    ranked_title_list_type = sgqlc.types.Field(sgqlc.types.non_null(RankedTitleListType), graphql_name='rankedTitleListType')



class RankedTitleListSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_ranked_title_lists', 'exclude_ranked_title_lists')
    all_ranked_title_lists = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RankedTitleList)), graphql_name='allRankedTitleLists')

    exclude_ranked_title_lists = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RankedTitleList)), graphql_name='excludeRankedTitleLists')



class RatingValueConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('type', 'value')
    type = sgqlc.types.Field(sgqlc.types.non_null(RatingsCondition), graphql_name='type')

    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')



class RatingsConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('ratings',)
    ratings = sgqlc.types.Field(RatingValueConstraint, graphql_name='ratings')



class RatingsSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(RatingsSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class RecentVideosQueryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('content_types',)
    content_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoContentTypeId)), graphql_name='contentTypes')



class RecommendedVideoTimedTextTrackFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('format', 'language')
    format = sgqlc.types.Field(VideoTimedTextTrackFormat, graphql_name='format')

    language = sgqlc.types.Field(Language, graphql_name='language')



class RegionCertificateRatingInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('rating', 'region')
    rating = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rating')

    region = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='region')



class ReleaseDateSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('release_date_range',)
    release_date_range = sgqlc.types.Field(DateRange, graphql_name='releaseDateRange')



class ReviewsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('author_rating', 'spoiler')
    author_rating = sgqlc.types.Field(Int, graphql_name='authorRating')

    spoiler = sgqlc.types.Field(FilterInclusion, graphql_name='spoiler')



class ReviewsSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(ReviewsSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class RuntimeSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('runtime_range_minutes',)
    runtime_range_minutes = sgqlc.types.Field(IntRangeInput, graphql_name='runtimeRangeMinutes')



class SelfVerifiedNameCreditTypeFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_types', 'include_types')
    exclude_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeTypes')

    include_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeTypes')



class SharedNamesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('credit_categories',)
    credit_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='creditCategories')



class SharedNamesInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('input', 'name_id')
    input = sgqlc.types.Field(sgqlc.types.non_null(NameNetworkAlgorithmType), graphql_name='input')

    name_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nameId')



class SharedTitlesInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('input', 'name_id')
    input = sgqlc.types.Field(sgqlc.types.non_null(NameNetworkAlgorithmType), graphql_name='input')

    name_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nameId')



class ShowtimesLocation(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('lat_long', 'postal_code', 'radius_in_meters')
    lat_long = sgqlc.types.Field(LatLong, graphql_name='latLong')

    postal_code = sgqlc.types.Field('ShowtimesPostalCodeLocation', graphql_name='postalCode')

    radius_in_meters = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='radiusInMeters')



class ShowtimesPostalCodeLocation(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('country', 'postal_code')
    country = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='country')

    postal_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='postalCode')



class ShowtimesTitlesCinemasMetadata(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_cinema_ids',)
    any_cinema_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyCinemaIds')



class ShowtimesTitlesDateRangeFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('end_time', 'start_time')
    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')

    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')



class ShowtimesTitlesQueryMetadata(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('date_range', 'sort_field', 'sort_order', 'ticketing_types')
    date_range = sgqlc.types.Field(ShowtimesTitlesDateRangeFilter, graphql_name='dateRange')

    sort_field = sgqlc.types.Field(sgqlc.types.non_null(ShowtimesTitlesSortField), graphql_name='sortField')

    sort_order = sgqlc.types.Field(sgqlc.types.non_null(ShowtimesTitlesSortOrder), graphql_name='sortOrder')

    ticketing_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TicketingType)), graphql_name='ticketingTypes')



class SingleUserRatingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('filter_type', 'rating_range', 'user_id')
    filter_type = sgqlc.types.Field(SingleUserRatingSearchFilterType, graphql_name='filterType')

    rating_range = sgqlc.types.Field(IntRangeInput, graphql_name='ratingRange')

    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')



class SoundMixSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_sound_mix_types', 'exclude_sound_mix_types')
    any_sound_mix_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anySoundMixTypes')

    exclude_sound_mix_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeSoundMixTypes')



class SoundtrackMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_soundtrack_text_terms', 'any_soundtrack_text_terms')
    all_soundtrack_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allSoundtrackTextTerms')

    any_soundtrack_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anySoundtrackTextTerms')



class StreamingTitlesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_title_types', 'max_providers', 'providers')
    include_title_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleTypeCategoryValue)), graphql_name='includeTitleTypes')

    max_providers = sgqlc.types.Field(Int, graphql_name='maxProviders')

    providers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='providers')



class SuggestionSearchFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('type',)
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SuggestionSearchType)), graphql_name='type')



class SymphonyMultiValueMapEntry(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')

    value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='value')



class TechnicalSpecificationsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('versions',)
    versions = sgqlc.types.Field(FilterVersions, graphql_name='versions')



class TitleChartRankingsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('rankings_chart_type',)
    rankings_chart_type = sgqlc.types.Field(sgqlc.types.non_null(TitleChartRankingsType), graphql_name='rankingsChartType')



class TitleCinemaShowtimesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('date_range', 'location')
    date_range = sgqlc.types.Field(ShowtimesTitlesDateRangeFilter, graphql_name='dateRange')

    location = sgqlc.types.Field(ShowtimesLocation, graphql_name='location')



class TitleCreditCategoryWithCreditsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('credited', 'exclude_principal', 'names')
    credited = sgqlc.types.Field(CreditedOrUncreditedFilter, graphql_name='credited')

    exclude_principal = sgqlc.types.Field(Boolean, graphql_name='excludePrincipal')

    names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='names')



class TitleCreditSearchInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('character', 'job_category', 'name_id')
    character = sgqlc.types.Field(String, graphql_name='character')

    job_category = sgqlc.types.Field(String, graphql_name='jobCategory')

    name_id = sgqlc.types.Field(ID, graphql_name='nameId')



class TitleCreditSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(TitleCreditSortBy, graphql_name='by')

    order = sgqlc.types.Field(SortOrder, graphql_name='order')



class TitleCreditsConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_credits', 'any_credits', 'exclude_credits')
    all_credits = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleCreditSearchInput)), graphql_name='allCredits')

    any_credits = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleCreditSearchInput)), graphql_name='anyCredits')

    exclude_credits = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleCreditSearchInput)), graphql_name='excludeCredits')



class TitleCreditsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'credited', 'exclude_categories', 'exclude_principal', 'names')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    credited = sgqlc.types.Field(CreditedOrUncreditedFilter, graphql_name='credited')

    exclude_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludeCategories')

    exclude_principal = sgqlc.types.Field(Boolean, graphql_name='excludePrincipal')

    names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='names')



class TitleKeywordItemCategoriesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('exclude_item_categories', 'item_categories')
    exclude_item_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeItemCategories')

    item_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='itemCategories')



class TitleKeywordsSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by',)
    by = sgqlc.types.Field(sgqlc.types.non_null(TitleKeywordsSortBy), graphql_name='by')



class TitleListSearchSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(TitleListSearchSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class TitleMeterRankingInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('meter_type',)
    meter_type = sgqlc.types.Field(TitleMeterType, graphql_name='meterType')



class TitleMeterSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('rank_range', 'title_meter_type')
    rank_range = sgqlc.types.Field(IntRangeInput, graphql_name='rankRange')

    title_meter_type = sgqlc.types.Field(TitleMeterType, graphql_name='titleMeterType')



class TitleQuoteMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_quote_text_terms', 'any_quote_text_terms')
    all_quote_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allQuoteTextTerms')

    any_quote_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyQuoteTextTerms')



class TitleQuotesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('names', 'spoilers')
    names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='names')

    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class TitleRecommendationsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_title_types',)
    include_title_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleTypeCategoryValue)), graphql_name='includeTitleTypes')



class TitleReleaseDatesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('countries', 'wide_release')
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='countries')

    wide_release = sgqlc.types.Field(WideReleaseFilter, graphql_name='wideRelease')



class TitleSearchOptions(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('release_date_range', 'type')
    release_date_range = sgqlc.types.Field(DateRange, graphql_name='releaseDateRange')

    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MainSearchTitleType)), graphql_name='type')



class TitleTextSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('search_term',)
    search_term = sgqlc.types.Field(String, graphql_name='searchTerm')



class TitleTriviaMatchingSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_trivia_text_terms', 'any_trivia_text_terms')
    all_trivia_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='allTriviaTextTerms')

    any_trivia_text_terms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyTriviaTextTerms')



class TitleTypeSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_title_type_ids', 'exclude_title_type_ids')
    any_title_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyTitleTypeIds')

    exclude_title_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeTitleTypeIds')



class TopGrossingReleasesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('time_window', 'top_grossing_releases_area')
    time_window = sgqlc.types.Field(sgqlc.types.non_null('TopGrossingReleasesTimeWindow'), graphql_name='timeWindow')

    top_grossing_releases_area = sgqlc.types.Field(sgqlc.types.non_null(BoxOfficeReleasesAreaFilter), graphql_name='topGrossingReleasesArea')



class TopGrossingReleasesTimeWindow(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('time_window_period',)
    time_window_period = sgqlc.types.Field(sgqlc.types.non_null(TopGrossingReleasesTimeWindowPeriod), graphql_name='timeWindowPeriod')



class TopMeterTitlesFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('genre_id', 'top_meter_titles_type')
    genre_id = sgqlc.types.Field(String, graphql_name='genreId')

    top_meter_titles_type = sgqlc.types.Field(TopMeterTitlesType, graphql_name='topMeterTitlesType')



class TopTrendingInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('data_window', 'traffic_source')
    data_window = sgqlc.types.Field(sgqlc.types.non_null(TrendingDataWindow), graphql_name='dataWindow')

    traffic_source = sgqlc.types.Field(sgqlc.types.non_null(TrendingTrafficSource), graphql_name='trafficSource')



class TopTrendingSetsPredefinedInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('top_trending_set_predefined',)
    top_trending_set_predefined = sgqlc.types.Field(sgqlc.types.non_null(TopTrendingPredefinedEnum), graphql_name='topTrendingSetPredefined')



class TrackRecommendationsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('profession',)
    profession = sgqlc.types.Field(String, graphql_name='profession')



class TriviaCategoryWithTriviaFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('spoilers',)
    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class TriviaFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('categories', 'spoilers')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='categories')

    spoilers = sgqlc.types.Field(FilterSpoilers, graphql_name='spoilers')



class UserConsentInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('consent_type', 'idfa')
    consent_type = sgqlc.types.Field(sgqlc.types.non_null(ConsentType), graphql_name='consentType')

    idfa = sgqlc.types.Field(String, graphql_name='idfa')



class UserInterestsFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_interest_ids',)
    include_interest_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeInterestIds')



class UserPreferredStreamingProvidersInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_filter',)
    include_filter = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='includeFilter')



class UserRatingsSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('aggregate_rating_range', 'ratings_count_range')
    aggregate_rating_range = sgqlc.types.Field(FloatRangeInput, graphql_name='aggregateRatingRange')

    ratings_count_range = sgqlc.types.Field(IntRangeInput, graphql_name='ratingsCountRange')



class UserReviewsInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('sort', 'user_id')
    sort = sgqlc.types.Field('UserReviewsSort', graphql_name='sort')

    user_id = sgqlc.types.Field(ID, graphql_name='userId')



class UserReviewsSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(UserReviewsSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class VideoAdFeedbackUrlInput(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('video_ad_xml',)
    video_ad_xml = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='videoAdXml')



class VideoContentFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('definitions', 'mime_types')
    definitions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoDefinition)), graphql_name='definitions')

    mime_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoMimeType)), graphql_name='mimeTypes')



class VideoNameFilterConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_name_ids',)
    all_name_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='allNameIds')



class VideoRecommendationsContext(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('display_type', 'supported_ad_types')
    display_type = sgqlc.types.Field(sgqlc.types.non_null(VideoRecommendationsDisplayType), graphql_name='displayType')

    supported_ad_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(VideoRecommendationsAdType))), graphql_name='supportedAdTypes')



class VideoSort(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(VideoSortBy), graphql_name='by')

    order = sgqlc.types.Field(sgqlc.types.non_null(SortOrder), graphql_name='order')



class VideoTimedTextTracksFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('format',)
    format = sgqlc.types.Field(VideoTimedTextTrackFormat, graphql_name='format')



class VideoTitleFilterConstraints(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_title_ids',)
    any_title_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='anyTitleIds')



class VideosQueryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('maturity_level', 'name_constraints', 'title_constraints', 'types')
    maturity_level = sgqlc.types.Field(MaturityLevel, graphql_name='maturityLevel')

    name_constraints = sgqlc.types.Field(VideoNameFilterConstraints, graphql_name='nameConstraints')

    title_constraints = sgqlc.types.Field(VideoTitleFilterConstraints, graphql_name='titleConstraints')

    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoContentTypeId)), graphql_name='types')



class ViewPortSize(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('height', 'width')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')

    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')



class WatchOptionQueryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_watch_option_categories',)
    include_watch_option_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(WatchOptionCategoryType)), graphql_name='includeWatchOptionCategories')



class WatchOptionsLocation(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('lat_long', 'postal_code_location')
    lat_long = sgqlc.types.Field(LatLong, graphql_name='latLong')

    postal_code_location = sgqlc.types.Field(PostalCodeLocation, graphql_name='postalCodeLocation')



class WatchOptionsSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('any_watch_provider_ids', 'any_watch_regions', 'exclude_watch_provider_ids', 'exclude_watch_regions', 'has_watch_option_types')
    any_watch_provider_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyWatchProviderIds')

    any_watch_regions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anyWatchRegions')

    exclude_watch_provider_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeWatchProviderIds')

    exclude_watch_regions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='excludeWatchRegions')

    has_watch_option_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SearchWatchOptionType)), graphql_name='hasWatchOptionTypes')



class WatchProvidersQueryFilter(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('include_watch_option_categories',)
    include_watch_option_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(WatchOptionCategoryType)), graphql_name='includeWatchOptionCategories')



class WithNameDataSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_data_available', 'any_data_available', 'no_data_available')
    all_data_available = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameDataType)), graphql_name='allDataAvailable')

    any_data_available = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameDataType)), graphql_name='anyDataAvailable')

    no_data_available = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameDataType)), graphql_name='noDataAvailable')



class WithTitleDataSearchConstraint(sgqlc.types.Input):
    __schema__ = model
    __field_names__ = ('all_data_available', 'any_data_available', 'no_data_available')
    all_data_available = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleDataType)), graphql_name='allDataAvailable')

    any_data_available = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleDataType)), graphql_name='anyDataAvailable')

    no_data_available = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleDataType)), graphql_name='noDataAvailable')




########################################################################
# Output Objects and Interfaces
########################################################################
class Connection(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Edge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')



class Consent(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('consent_operation', 'consent_type', 'expiration_date')
    consent_operation = sgqlc.types.Field(sgqlc.types.non_null(ConsentOperation), graphql_name='consentOperation')

    consent_type = sgqlc.types.Field(sgqlc.types.non_null(ConsentType), graphql_name='consentType')

    expiration_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='expirationDate')



class ContentRestriction(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('explanations', 'reasons', 'restriction_reason')
    explanations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RestrictionExplanation'))), graphql_name='explanations')

    reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContentRestrictionReason))), graphql_name='reasons')

    restriction_reason = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContentRestrictionReason))), graphql_name='restrictionReason')



class Credit(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('category', 'name', 'title')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class DisplayableConcept(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('id', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class DisplayableProperty(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='value')



class DisplayableSearchResult(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('display_labels', 'image', 'release_year')
    display_labels = sgqlc.types.Field('DisplayLabels', graphql_name='displayLabels')

    image = sgqlc.types.Field('ImageObject', graphql_name='image')

    release_year = sgqlc.types.Field('YearRange', graphql_name='releaseYear')



class Edge(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('cursor',)
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')



class ExperimentalCredit(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('category', 'name', 'title')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class Experimental_UIWorkflowFormElement(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('help_link', 'id', 'label')
    help_link = sgqlc.types.Field('Experimental_UIWorkflowHelpLink', graphql_name='helpLink')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    label = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='label')



class Experimental_UIWorkflowFormElementWithFeedback(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('feedback', 'help_link', 'id', 'label')
    feedback = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_UIWorkflowFeedbackElement')), graphql_name='feedback')

    help_link = sgqlc.types.Field('Experimental_UIWorkflowHelpLink', graphql_name='helpLink')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    label = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='label')



class Experimental_UIWorkflowFormInputElement(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('input_type',)
    input_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowFormInputType), graphql_name='inputType')



class ExportDetail(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('expires_on', 'export_type', 'result_url', 'started_on', 'status', 'total_exported_objects')
    expires_on = sgqlc.types.Field(DateTime, graphql_name='expiresOn')

    export_type = sgqlc.types.Field(sgqlc.types.non_null(ExportType), graphql_name='exportType')

    result_url = sgqlc.types.Field(URL, graphql_name='resultUrl')

    started_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startedOn')

    status = sgqlc.types.Field(sgqlc.types.non_null('ExportStatus'), graphql_name='status')

    total_exported_objects = sgqlc.types.Field(Int, graphql_name='totalExportedObjects')



class HasDisplayableArticle(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('displayable_article',)
    displayable_article = sgqlc.types.Field('DisplayableArticle', graphql_name='displayableArticle')



class HasDisplayableProperty(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('displayable_property',)
    displayable_property = sgqlc.types.Field(sgqlc.types.non_null(DisplayableProperty), graphql_name='displayableProperty')



class HasDisplayablePropertyKey(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('key',)
    key = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='key')



class HasDisplayableQualifier(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('qualifiers_in_markdown_list',)
    qualifiers_in_markdown_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Markdown')), graphql_name='qualifiersInMarkdownList')



class ImageObject(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('height', 'url', 'width')
    height = sgqlc.types.Field(Int, graphql_name='height')

    url = sgqlc.types.Field(String, graphql_name='url')

    width = sgqlc.types.Field(Int, graphql_name='width')



class Link(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('label', 'url')
    label = sgqlc.types.Field(String, graphql_name='label')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')



class LocalizedDisplayableConcept(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('id', 'language', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class ManagedCompanyKnownForCategory(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('status',)
    status = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForStatus), graphql_name='status')



class ManagedCompanyKnownForCategoryVersion(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('created_date', 'modified_by', 'status', 'version_number')
    created_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='createdDate')

    modified_by = sgqlc.types.Field('ModifiedBy', graphql_name='modifiedBy')

    status = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForStatus), graphql_name='status')

    version_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='versionNumber')



class Meta(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('canonical_id', 'publication_status')
    canonical_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='canonicalId')

    publication_status = sgqlc.types.Field(sgqlc.types.non_null(PublicationStatus), graphql_name='publicationStatus')



class MeterRanking(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('current_rank', 'rank_change')
    current_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentRank')

    rank_change = sgqlc.types.Field('MeterRankChange', graphql_name='rankChange')



class MeterRankingHistory(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('best_rank', 'ranks', 'restriction')
    best_rank = sgqlc.types.Field('MeterRankingHistoryEntry', graphql_name='bestRank')

    ranks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MeterRankingHistoryEntry')), graphql_name='ranks')

    restriction = sgqlc.types.Field('MeterRestriction', graphql_name='restriction')



class PrimaryConst(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class PublicityListingType(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('category',)
    category = sgqlc.types.Field(sgqlc.types.non_null('PublicityListingCategory'), graphql_name='category')



class Score(sgqlc.types.Interface):
    __schema__ = model
    __field_names__ = ('current_score',)
    current_score = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentScore')



class ActionLink(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('label', 'url')
    label = sgqlc.types.Field('CallToActionText', graphql_name='label')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')



class AdCreativeInfo(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('size', 'slot_markup')
    size = sgqlc.types.Field(sgqlc.types.non_null('CreativeSize'), graphql_name='size')

    slot_markup = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slotMarkup')



class AdSlot(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('ad_feedback_url', 'creative_info', 'name')
    ad_feedback_url = sgqlc.types.Field(URL, graphql_name='adFeedbackUrl')

    creative_info = sgqlc.types.Field(sgqlc.types.non_null(AdCreativeInfo), graphql_name='creativeInfo')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')



class AdvancedNameSearchResult(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')



class AdvancedTitleSearchResult(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title',)
    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class AgePlayingRange(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('from_', 'to')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='from')

    to = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='to')



class AggregateRatingsBreakdown(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('histogram', 'is_collapsed', 'ratings_summary_by_country', 'ratings_summary_by_demographics')
    histogram = sgqlc.types.Field('Histogram', graphql_name='histogram', args=sgqlc.types.ArgDict((
        ('demographic_filter', sgqlc.types.Arg(DemographicFilter, graphql_name='demographicFilter', default={'userCategory': 'IMDB_USERS'})),
))
    )
    '''Arguments:

    * `demographic_filter` (`DemographicFilter`)None (default:
      `{userCategory: IMDB_USERS}`)
    '''

    is_collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCollapsed')

    ratings_summary_by_country = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RatingsSummaryByCountry')), graphql_name='ratingsSummaryByCountry', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    ratings_summary_by_demographics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DemographicRatings')), graphql_name='ratingsSummaryByDemographics')



class AlexaQuestion(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('answer', 'attribute_id', 'question')
    answer = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='answer')

    attribute_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='attributeId')

    question = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='question')



class AlexaQuestionConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AlexaQuestionEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AlexaQuestionEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(AlexaQuestion), graphql_name='node')



class AmazonMusicProduct(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('amazon_id', 'artists', 'format', 'image', 'product_title')
    amazon_id = sgqlc.types.Field(sgqlc.types.non_null('AmazonStandardId'), graphql_name='amazonId')

    artists = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AmazonMusicProductArtist')), graphql_name='artists')

    format = sgqlc.types.Field(sgqlc.types.non_null('AmazonMusicProductFormat'), graphql_name='format')

    image = sgqlc.types.Field('Image', graphql_name='image')

    product_title = sgqlc.types.Field(sgqlc.types.non_null('AmazonMusicProductTitle'), graphql_name='productTitle')



class AmazonMusicProductArtist(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('artist_name',)
    artist_name = sgqlc.types.Field(sgqlc.types.non_null('AmazonMusicProductArtistName'), graphql_name='artistName')



class AmazonStandardId(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('asin', 'obfuscated_marketplace_id', 'region')
    asin = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='asin')

    obfuscated_marketplace_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='obfuscatedMarketplaceId')

    region = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='region')



class AspectRatios(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AspectRatio'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AuthProviderDeprecationMessage(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('message', 'urls')
    message = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='message')

    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AuthProviderDeprecationUrl'))), graphql_name='urls')



class AuthProviderDeprecationUrl(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null('AuthProviderDeprecationUrlLabel'), graphql_name='label')

    value = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='value')



class AwardCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(String, graphql_name='text')



class AwardNomination(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award', 'awarded_entities', 'category', 'for_episodes', 'for_song_titles', 'id', 'is_winner', 'notes', 'win_announcement_date', 'winning_rank')
    award = sgqlc.types.Field(sgqlc.types.non_null('AwardDetails'), graphql_name='award')

    awarded_entities = sgqlc.types.Field(sgqlc.types.non_null('AwardedEntities'), graphql_name='awardedEntities')

    category = sgqlc.types.Field(AwardCategory, graphql_name='category')

    for_episodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Title')), graphql_name='forEpisodes')

    for_song_titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='forSongTitles')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_winner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isWinner')

    notes = sgqlc.types.Field('Markdown', graphql_name='notes')

    win_announcement_date = sgqlc.types.Field('DisplayableDate', graphql_name='winAnnouncementDate')

    winning_rank = sgqlc.types.Field(Int, graphql_name='winningRank')



class AwardNominationsWithCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_nominations', 'category')
    award_nominations = sgqlc.types.Field('AwardNominationConnection', graphql_name='awardNominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(AwardNominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(AwardNominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`AwardNominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`AwardNominationsSort`)None
    '''

    category = sgqlc.types.Field(AwardCategory, graphql_name='category')



class AwardedNames(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_names', 'secondary_award_companies', 'secondary_award_titles')
    award_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AwardName'))), graphql_name='awardNames')

    secondary_award_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AwardCompany')), graphql_name='secondaryAwardCompanies')

    secondary_award_titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AwardTitle')), graphql_name='secondaryAwardTitles')



class AwardedTitles(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_titles', 'secondary_award_companies', 'secondary_award_names')
    award_titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AwardTitle'))), graphql_name='awardTitles')

    secondary_award_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AwardCompany')), graphql_name='secondaryAwardCompanies')

    secondary_award_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AwardName')), graphql_name='secondaryAwardNames')



class BoxOfficeGross(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null('Money'), graphql_name='total')



class BoxOfficeRelease(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('titles', 'weeks_running')
    titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Title'))), graphql_name='titles')

    weeks_running = sgqlc.types.Field(Int, graphql_name='weeksRunning')



class BoxOfficeWeekendChart(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('entries', 'weekend_end_date', 'weekend_start_date')
    entries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ChartEntry'))), graphql_name='entries')

    weekend_end_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='weekendEndDate')

    weekend_start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='weekendStartDate')



class CallToAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('landing_page_pro', 'name_banner', 'name_claim_page_for_free', 'name_discover_more_insights', 'name_images_reels', 'name_pro_upsell', 'name_view_star_meter', 'navbar_pro_flyout', 'title_pro_upsell')
    landing_page_pro = sgqlc.types.Field('LinkCallToAction', graphql_name='landingPagePro', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    name_banner = sgqlc.types.Field('MarkdownSlotCallToAction', graphql_name='nameBanner', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    name_claim_page_for_free = sgqlc.types.Field('SectionCallToAction', graphql_name='nameClaimPageForFree', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    name_discover_more_insights = sgqlc.types.Field('LinkCallToAction', graphql_name='nameDiscoverMoreInsights', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    name_images_reels = sgqlc.types.Field('LinkCallToAction', graphql_name='nameImagesReels', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    name_pro_upsell = sgqlc.types.Field('MultiLinkCallToAction', graphql_name='nameProUpsell', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    name_view_star_meter = sgqlc.types.Field('LinkCallToAction', graphql_name='nameViewStarMeter', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    navbar_pro_flyout = sgqlc.types.Field('ImageAndLinkCallToAction', graphql_name='navbarProFlyout', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''

    title_pro_upsell = sgqlc.types.Field('LinkCallToAction', graphql_name='titleProUpsell', args=sgqlc.types.ArgDict((
        ('result_override', sgqlc.types.Arg(ResultID, graphql_name='resultOverride', default=None)),
))
    )
    '''Arguments:

    * `result_override` (`ResultID`)None
    '''



class CallToActionText(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'language', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class Cameras(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Camera'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CanRate(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_ratable',)
    is_ratable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRatable')



class CategorizedWatchOptions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category_name', 'watch_options')
    category_name = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='categoryName')

    watch_options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WatchOption'))), graphql_name='watchOptions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class CategorizedWatchOptionsList(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('categorized_watch_options_list',)
    categorized_watch_options_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CategorizedWatchOptions))), graphql_name='categorizedWatchOptionsList')



class Certificate(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('attributes', 'country', 'id', 'rating', 'rating_reason', 'ratings_body', 'ratings_body_certificate_id')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DisplayableAttribute'))), graphql_name='attributes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    country = sgqlc.types.Field(sgqlc.types.non_null('DisplayableCountry'), graphql_name='country')

    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')

    rating = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rating')

    rating_reason = sgqlc.types.Field(String, graphql_name='ratingReason')

    ratings_body = sgqlc.types.Field('RatingsBody', graphql_name='ratingsBody')

    ratings_body_certificate_id = sgqlc.types.Field(String, graphql_name='ratingsBodyCertificateId')



class ChartEntry(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title', 'weekend_gross')
    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')

    weekend_gross = sgqlc.types.Field(sgqlc.types.non_null(BoxOfficeGross), graphql_name='weekendGross')



class Cinema(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('accessibility', 'contact_details', 'id', 'location', 'name')
    accessibility = sgqlc.types.Field('CinemaAccessibility', graphql_name='accessibility')

    contact_details = sgqlc.types.Field('CinemaContactDetails', graphql_name='contactDetails')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    location = sgqlc.types.Field('CinemaLocation', graphql_name='location')

    name = sgqlc.types.Field('CinemaName', graphql_name='name')



class CinemaAccessibility(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('audio_accessibility', 'wheelchair_accessibility')
    audio_accessibility = sgqlc.types.Field('CinemaAudioAccessibility', graphql_name='audioAccessibility')

    wheelchair_accessibility = sgqlc.types.Field('CinemaWheelchairAccessibility', graphql_name='wheelchairAccessibility')



class CinemaAudioAccessibility(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('has_hearing_devices',)
    has_hearing_devices = sgqlc.types.Field(Boolean, graphql_name='hasHearingDevices')



class CinemaContactDetails(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('phone_number',)
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')



class CinemaWheelchairAccessibility(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('has_wheelchair_access',)
    has_wheelchair_access = sgqlc.types.Field(Boolean, graphql_name='hasWheelchairAccess')



class ClaimedName(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name', 'status')
    name = sgqlc.types.Field('Name', graphql_name='name')

    status = sgqlc.types.Field(sgqlc.types.non_null(ClaimedNameStatus), graphql_name='status')



class Colorations(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Coloration'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyCreditCategoryWithCompanyCredits(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'company_credits', 'restriction')
    category = sgqlc.types.Field('CompanyCreditCategory', graphql_name='category')

    company_credits = sgqlc.types.Field('CompanyCreditConnection', graphql_name='companyCredits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    restriction = sgqlc.types.Field('CompanyCreditRestriction', graphql_name='restriction')



class CompanyEmployment(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('branch', 'occupation', 'title')
    branch = sgqlc.types.Field('EmployeeBranchName', graphql_name='branch')

    occupation = sgqlc.types.Field(sgqlc.types.non_null('CompanyEmployeeOccupation'), graphql_name='occupation')

    title = sgqlc.types.Field(sgqlc.types.non_null('CompanyEmployeeTitle'), graphql_name='title')



class CompanyKeyStaff(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name', 'summary')
    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    summary = sgqlc.types.Field(sgqlc.types.non_null('CompanyKeyStaffSummary'), graphql_name='summary')



class CompanyKeyStaffSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('employment',)
    employment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyEmployment)), graphql_name='employment', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    '''



class CompanyKnownForClient(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name', 'summary')
    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    summary = sgqlc.types.Field(sgqlc.types.non_null('CompanyKnownForClientSummary'), graphql_name='summary')



class CompanyKnownForClientSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('representation', 'representation_categories')
    representation = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompanyRepresentationCategory')), graphql_name='representation', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    representation_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompanyRepresentationCategories')), graphql_name='representationCategories')



class CompanyKnownForJob(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'job')
    category = sgqlc.types.Field(sgqlc.types.non_null('CompanyKnownForCreditCategory'), graphql_name='category')

    job = sgqlc.types.Field('CompanyJob', graphql_name='job')



class CompanyKnownForTitle(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('summary', 'title')
    summary = sgqlc.types.Field(sgqlc.types.non_null('CompanyKnownForTitleSummary'), graphql_name='summary')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class CompanyKnownForTitleSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('countries', 'jobs', 'year_range')
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DisplayableCountry')), graphql_name='countries')

    jobs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyKnownForJob))), graphql_name='jobs')

    year_range = sgqlc.types.Field('YearRange', graphql_name='yearRange')



class CompanyMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('company_credit_categories',)
    company_credit_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompanyCreditCategory'))), graphql_name='companyCreditCategories')



class CompanyText(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class ConnectionCategoryWithConnections(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'connections')
    category = sgqlc.types.Field(sgqlc.types.non_null('TitleConnectionCategory'), graphql_name='category')

    connections = sgqlc.types.Field('TitleConnectionConnection', graphql_name='connections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class ContentWarnings(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_primarily_adult_actor',)
    is_primarily_adult_actor = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrimarilyAdultActor')



class ContributionLink(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')



class ContributionQuestionsLink(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')



class Contributor(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    user = sgqlc.types.Field('UserProfile', graphql_name='user')



class ContributorLeaderboard(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('description', 'id', 'is_finalized', 'last_updated', 'leaderboard_url', 'month', 'period', 'rankings', 'title', 'total_approved_items', 'total_contributors', 'year')
    description = sgqlc.types.Field('LocalizedString', graphql_name='description')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_finalized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFinalized')

    last_updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastUpdated')

    leaderboard_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='leaderboardUrl')

    month = sgqlc.types.Field(Int, graphql_name='month')

    period = sgqlc.types.Field(sgqlc.types.non_null('ContributorLeaderboardPeriodType'), graphql_name='period')

    rankings = sgqlc.types.Field(sgqlc.types.non_null('ContributorRankingsConnection'), graphql_name='rankings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ContributorLeaderboardRankingsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(ContributorRankSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ContributorLeaderboardRankingsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`ContributorRankSort`)None
    '''

    title = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='title')

    total_approved_items = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalApprovedItems')

    total_contributors = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalContributors')

    year = sgqlc.types.Field(Int, graphql_name='year')



class ContributorLeaderboardPeriodType(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ContributorLeaderboardPeriodTypeId), graphql_name='id')



class ContributorLeaderboardRank(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('leaderboard', 'ranking')
    leaderboard = sgqlc.types.Field(sgqlc.types.non_null(ContributorLeaderboard), graphql_name='leaderboard')

    ranking = sgqlc.types.Field(sgqlc.types.non_null('ContributorRank'), graphql_name='ranking')



class ContributorLeaderboards(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('all', 'all_time', 'month', 'months', 'year', 'years')
    all = sgqlc.types.Field(sgqlc.types.non_null('ContributorLeaderboardConnection'), graphql_name='all', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    all_time = sgqlc.types.Field(ContributorLeaderboard, graphql_name='allTime')

    month = sgqlc.types.Field(ContributorLeaderboard, graphql_name='month', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='month', default=None)),
        ('year', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='year', default=None)),
))
    )
    '''Arguments:

    * `month` (`Int!`)None
    * `year` (`Int!`)None
    '''

    months = sgqlc.types.Field(sgqlc.types.non_null('ContributorLeaderboardConnection'), graphql_name='months', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(ContributorLeaderboardsByMonthFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ContributorLeaderboardsByMonthFilter`)None
    * `first` (`Int`)None
    '''

    year = sgqlc.types.Field(ContributorLeaderboard, graphql_name='year', args=sgqlc.types.ArgDict((
        ('year', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='year', default=None)),
))
    )
    '''Arguments:

    * `year` (`Int!`)None
    '''

    years = sgqlc.types.Field(sgqlc.types.non_null('ContributorLeaderboardConnection'), graphql_name='years', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(ContributorLeaderboardsByYearFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ContributorLeaderboardsByYearFilter`)None
    * `first` (`Int`)None
    '''



class ContributorRank(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('approved_items', 'approved_items_delta', 'contributor', 'id', 'rank', 'rank_delta')
    approved_items = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='approvedItems')

    approved_items_delta = sgqlc.types.Field(Int, graphql_name='approvedItemsDelta')

    contributor = sgqlc.types.Field(Contributor, graphql_name='contributor')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')

    rank_delta = sgqlc.types.Field(Int, graphql_name='rankDelta')



class CountriesOfOrigin(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('countries', 'language')
    countries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CountryOfOrigin'))), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')



class CountryAttributeMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('limit', 'valid_values')
    limit = sgqlc.types.Field(Int, graphql_name='limit')

    valid_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LocalizedDisplayableCountry'))), graphql_name='validValues')



class CreativeSize(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('height', 'width')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')

    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')



class CreditCategorySummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'total')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CroppingParameters(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('height', 'width', 'x_offset', 'y_offset')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')

    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')

    x_offset = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='xOffset')

    y_offset = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='yOffset')



class CustomFeaturedImages(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('images', 'is_admin_edited', 'is_admin_notification_seen', 'is_blocked', 'is_published', 'is_reset', 'last_edited', 'last_edited_by_admin')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Image')), graphql_name='images')

    is_admin_edited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminEdited')

    is_admin_notification_seen = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminNotificationSeen')

    is_blocked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBlocked')

    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')

    is_reset = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isReset')

    last_edited = sgqlc.types.Field(DateTime, graphql_name='lastEdited')

    last_edited_by_admin = sgqlc.types.Field(DateTime, graphql_name='lastEditedByAdmin')



class CustomKnownFor(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_admin_edited', 'is_admin_notification_seen', 'is_blocked', 'is_published', 'is_reset', 'last_edited', 'last_edited_by_admin', 'titles')
    is_admin_edited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminEdited')

    is_admin_notification_seen = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminNotificationSeen')

    is_blocked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBlocked')

    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')

    is_reset = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isReset')

    last_edited = sgqlc.types.Field(DateTime, graphql_name='lastEdited')

    last_edited_by_admin = sgqlc.types.Field(DateTime, graphql_name='lastEditedByAdmin')

    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Title')), graphql_name='titles')



class CustomPrimaryImage(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('image_edit_parameters', 'original_image')
    image_edit_parameters = sgqlc.types.Field('ImageEditParameters', graphql_name='imageEditParameters')

    original_image = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='originalImage')



class CustomPrimaryProfessions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_admin_edited', 'is_admin_notification_seen', 'is_blocked', 'is_published', 'is_reset', 'last_edited', 'last_edited_by_admin', 'professions')
    is_admin_edited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminEdited')

    is_admin_notification_seen = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminNotificationSeen')

    is_blocked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBlocked')

    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')

    is_reset = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isReset')

    last_edited = sgqlc.types.Field(DateTime, graphql_name='lastEdited')

    last_edited_by_admin = sgqlc.types.Field(DateTime, graphql_name='lastEditedByAdmin')

    professions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PrimaryProfession')), graphql_name='professions')



class DateComponents(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('day', 'is_approximate', 'is_bce', 'month', 'partial_year', 'year')
    day = sgqlc.types.Field(Int, graphql_name='day')

    is_approximate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproximate')

    is_bce = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBCE')

    month = sgqlc.types.Field(Int, graphql_name='month')

    partial_year = sgqlc.types.Field(String, graphql_name='partialYear')

    year = sgqlc.types.Field(Int, graphql_name='year')



class Demographic(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('age', 'country', 'display_text', 'gender', 'user_category')
    age = sgqlc.types.Field(Age, graphql_name='age')

    country = sgqlc.types.Field(Country, graphql_name='country')

    display_text = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='displayText')

    gender = sgqlc.types.Field(Gender, graphql_name='gender')

    user_category = sgqlc.types.Field(UserCategory, graphql_name='userCategory')



class DemographicDataItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('self_verified', 'type', 'value')
    self_verified = sgqlc.types.Field(sgqlc.types.non_null('SelfVerified'), graphql_name='selfVerified')

    type = sgqlc.types.Field(sgqlc.types.non_null('DemographicDataType'), graphql_name='type')

    value = sgqlc.types.Field(sgqlc.types.non_null('DemographicDataValue'), graphql_name='value')



class DemographicRatings(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('aggregate', 'demographic', 'vote_count')
    aggregate = sgqlc.types.Field(Float, graphql_name='aggregate')

    demographic = sgqlc.types.Field(sgqlc.types.non_null(Demographic), graphql_name='demographic')

    vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='voteCount')



class Disambiguation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('number', 'text')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class DisplayLabels(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('primary_label', 'secondary_label')
    primary_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='primaryLabel')

    secondary_label = sgqlc.types.Field(String, graphql_name='secondaryLabel')



class DisplayableArticle(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('body', 'footer', 'header')
    body = sgqlc.types.Field('Markdown', graphql_name='body')

    footer = sgqlc.types.Field('Markdown', graphql_name='footer')

    header = sgqlc.types.Field('Markdown', graphql_name='header')



class DisplayableAttribute(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'text')
    id = sgqlc.types.Field(ID, graphql_name='id')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class DisplayableDateRange(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('end_date', 'start_date')
    end_date = sgqlc.types.Field('DisplayableDate', graphql_name='endDate')

    start_date = sgqlc.types.Field('DisplayableDate', graphql_name='startDate')



class DisplayableEpisodeNumber(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('displayable_season', 'episode_number')
    displayable_season = sgqlc.types.Field(sgqlc.types.non_null('LocalizedDisplayableSeason'), graphql_name='displayableSeason')

    episode_number = sgqlc.types.Field(sgqlc.types.non_null('LocalizedDisplayableEpisodeNumber'), graphql_name='episodeNumber')



class DisplayablePrompt(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('const_id', 'display', 'prompt_type')
    const_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='constId')

    display = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='display')

    prompt_type = sgqlc.types.Field(sgqlc.types.non_null(PromptType), graphql_name='promptType')



class EngagementStatistics(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('follower_statistics', 'watchlist_statistics')
    follower_statistics = sgqlc.types.Field('FollowerStatistics', graphql_name='followerStatistics')

    watchlist_statistics = sgqlc.types.Field('WatchlistStatistics', graphql_name='watchlistStatistics')



class Episodes(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('displayable_seasons', 'displayable_years', 'episodes', 'is_ongoing')
    displayable_seasons = sgqlc.types.Field('DisplayableSeasonConnection', graphql_name='displayableSeasons', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    displayable_years = sgqlc.types.Field('DisplayableYearConnection', graphql_name='displayableYears', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    episodes = sgqlc.types.Field('EpisodeConnection', graphql_name='episodes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(EpisodesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(EpisodesSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`EpisodesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`EpisodesSort`)None
    '''

    is_ongoing = sgqlc.types.Field(Boolean, graphql_name='isOngoing')



class EventEdition(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('awards', 'event', 'id', 'instance_within_year', 'trivia', 'year')
    awards = sgqlc.types.Field('AwardDetailsConnection', graphql_name='awards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    event = sgqlc.types.Field(sgqlc.types.non_null('AwardsEvent'), graphql_name='event')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    instance_within_year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instanceWithinYear')

    trivia = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Markdown')), graphql_name='trivia')

    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')



class EventEditionAward(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_name', 'id', 'winners')
    award_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='awardName')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    winners = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AwardNomination))), graphql_name='winners', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class EventLiveResults(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('display_description', 'display_title', 'event_edition_award', 'event_id', 'event_page_url', 'no_winners_blurb')
    display_description = sgqlc.types.Field('LocalizedString', graphql_name='displayDescription')

    display_title = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='displayTitle')

    event_edition_award = sgqlc.types.Field(sgqlc.types.non_null(EventEditionAward), graphql_name='eventEditionAward')

    event_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventId')

    event_page_url = sgqlc.types.Field(URL, graphql_name='eventPageUrl')

    no_winners_blurb = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='noWinnersBlurb')



class EventMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('event', 'events')
    event = sgqlc.types.Field('AwardsEvent', graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    events = sgqlc.types.Field('EventConnection', graphql_name='events', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class EventUrl(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'url')
    category = sgqlc.types.Field(sgqlc.types.non_null('EventUrlCategory'), graphql_name='category')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')



class ExperimentalNameCreditCategoryWithCredits(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'credits')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    credits = sgqlc.types.Field('ExperimentalNameCreditConnection', graphql_name='credits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class ExperimentalNomination(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award', 'awarded_entities', 'category', 'event', 'event_edition', 'for_episodes', 'for_song_titles', 'id', 'is_winner', 'notes', 'winning_rank')
    award = sgqlc.types.Field('ExperimentalNominationAward', graphql_name='award')

    awarded_entities = sgqlc.types.Field('AwardedEntities', graphql_name='awardedEntities')

    category = sgqlc.types.Field(AwardCategory, graphql_name='category')

    event = sgqlc.types.Field('ExperimentalNominationEvent', graphql_name='event')

    event_edition = sgqlc.types.Field('ExperimentalNominationEventEdition', graphql_name='eventEdition')

    for_episodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Title')), graphql_name='forEpisodes')

    for_song_titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='forSongTitles')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_winner = sgqlc.types.Field(Boolean, graphql_name='isWinner')

    notes = sgqlc.types.Field('Markdown', graphql_name='notes')

    winning_rank = sgqlc.types.Field(Int, graphql_name='winningRank')



class ExperimentalNominationEvent(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('awards', 'editions', 'id', 'location', 'text', 'trivia', 'urls')
    awards = sgqlc.types.Field(sgqlc.types.list_of('ExperimentalNominationAward'), graphql_name='awards', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    editions = sgqlc.types.Field(sgqlc.types.list_of('ExperimentalNominationEventEdition'), graphql_name='editions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    location = sgqlc.types.Field('DisplayableLocation', graphql_name='location')

    text = sgqlc.types.Field(String, graphql_name='text')

    trivia = sgqlc.types.Field(sgqlc.types.list_of('Markdown'), graphql_name='trivia')

    urls = sgqlc.types.Field(sgqlc.types.list_of(EventUrl), graphql_name='urls')



class ExperimentalNominationEventEdition(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('awards', 'event', 'id', 'instance_within_year', 'trivia', 'year')
    awards = sgqlc.types.Field(sgqlc.types.list_of('ExperimentalNominationAward'), graphql_name='awards', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    event = sgqlc.types.Field(ExperimentalNominationEvent, graphql_name='event')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    instance_within_year = sgqlc.types.Field(Int, graphql_name='instanceWithinYear')

    trivia = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Markdown')), graphql_name='trivia')

    year = sgqlc.types.Field(Int, graphql_name='year')



class ExperimentalNominationsWithCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_nominations', 'category')
    award_nominations = sgqlc.types.Field('ExperimentalNominationConnection', graphql_name='awardNominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(AwardNominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(AwardNominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`AwardNominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`AwardNominationsSort`)None
    '''

    category = sgqlc.types.Field(AwardCategory, graphql_name='category')



class Experimental_AdditionalCreditItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('details', 'id', 'job', 'title')
    details = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='details')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    job = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='job')

    title = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='title')



class Experimental_AdditionalCreditItemConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_AdditionalCreditItemEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_AdditionalCreditItemEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(Experimental_AdditionalCreditItem), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_AdditionalResumeInfo(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('details', 'id', 'title')
    details = sgqlc.types.Field('LocalizedString', graphql_name='details')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    title = sgqlc.types.Field('LocalizedString', graphql_name='title')



class Experimental_AdditionalResumeInfoConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_AdditionalResumeInfoEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_AdditionalResumeInfoEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(Experimental_AdditionalResumeInfo), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_BooleanConstraint(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('error_message', 'value')
    error_message = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='errorMessage')

    value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='value')



class Experimental_IntThresholdConstraint(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('comparator', 'error_message', 'value')
    comparator = sgqlc.types.Field(Experimental_NumericThresholdComparator, graphql_name='comparator')

    error_message = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='errorMessage')

    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')



class Experimental_Kenobi(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('says',)
    says = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='says')



class Experimental_KeywordItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'keyword', 'keyword_const_id')
    category = sgqlc.types.Field(String, graphql_name='category')

    keyword = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='keyword')

    keyword_const_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='keyword_const_id')



class Experimental_MediaUploadDestination(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('upload_destinations',)
    upload_destinations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_UploadDestination'))), graphql_name='uploadDestinations')



class Experimental_NotificationPreference(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('interested', 'type')
    interested = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='interested')

    type = sgqlc.types.Field(sgqlc.types.non_null('Experimental_NotificationPreferenceType'), graphql_name='type')



class Experimental_RadioGroupFormConstraints(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_required',)
    is_required = sgqlc.types.Field(Experimental_BooleanConstraint, graphql_name='isRequired')



class Experimental_RadioOption(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('text', 'value')
    text = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='text')

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')



class Experimental_Resume(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('experimental_additional_awards', 'experimental_additional_credit_categories', 'experimental_additional_credits', 'experimental_additional_resume_info', 'experimental_education', 'experimental_performer_details', 'experimental_physical_attributes', 'experimental_references', 'experimental_skills', 'experimental_training')
    experimental_additional_awards = sgqlc.types.Field('Experimental_SelfVerifiedAwardConnection', graphql_name='experimental_additionalAwards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    experimental_additional_credit_categories = sgqlc.types.Field('Experimental_ResumeAdditionalCreditsCategories', graphql_name='experimental_additionalCreditCategories', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(Experimental_AdditionalCreditCategoriesInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`Experimental_AdditionalCreditCategoriesInput`)None
    '''

    experimental_additional_credits = sgqlc.types.Field(Experimental_AdditionalCreditItemConnection, graphql_name='experimental_additionalCredits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(Experimental_AdditionalCreditsInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    * `input` (`Experimental_AdditionalCreditsInput`)None
    '''

    experimental_additional_resume_info = sgqlc.types.Field(Experimental_AdditionalResumeInfoConnection, graphql_name='experimental_additionalResumeInfo', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    experimental_education = sgqlc.types.Field('Experimental_SelfVerifiedEducationConnection', graphql_name='experimental_education', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    experimental_performer_details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_ResumeDataItem')), graphql_name='experimental_performerDetails', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    experimental_physical_attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_ResumeDataItem')), graphql_name='experimental_physicalAttributes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    experimental_references = sgqlc.types.Field('Experimental_SelfVerifiedReferenceConnection', graphql_name='experimental_references', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    experimental_skills = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_ResumeDataItem')), graphql_name='experimental_skills', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    experimental_training = sgqlc.types.Field('Experimental_SelfVerifiedTrainingConnection', graphql_name='experimental_training', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''



class Experimental_ResumeAdditionalCreditsCategories(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('categories', 'total')
    categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_ResumeAdditionalCreditsCategory'))), graphql_name='categories')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_ResumeAdditionalCreditsCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('credits', 'id', 'title', 'total')
    credits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Experimental_AdditionalCreditItem))), graphql_name='credits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    title = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='title')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_ResumeDataItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null('Experimental_ResumeDataItemLabel'), graphql_name='label')

    value = sgqlc.types.Field('Experimental_ResumeDataItemValue', graphql_name='value')



class Experimental_ResumeDataItemLabel(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('qualifiers', 'value')
    qualifiers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LocalizedString')), graphql_name='qualifiers')

    value = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='value')



class Experimental_ResumeDataItemValue(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('qualifiers', 'value')
    qualifiers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LocalizedString')), graphql_name='qualifiers')

    value = sgqlc.types.Field('LocalizedString', graphql_name='value')



class Experimental_SelfVerifiedAward(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_title', 'details', 'event', 'id', 'year')
    award_title = sgqlc.types.Field('LocalizedString', graphql_name='awardTitle')

    details = sgqlc.types.Field('LocalizedString', graphql_name='details')

    event = sgqlc.types.Field('LocalizedString', graphql_name='event')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    year = sgqlc.types.Field(Int, graphql_name='year')



class Experimental_SelfVerifiedAwardConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_SelfVerifiedAwardEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_SelfVerifiedAwardEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(Experimental_SelfVerifiedAward), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_SelfVerifiedEducation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('degree', 'details', 'id', 'location', 'school', 'year')
    degree = sgqlc.types.Field('LocalizedString', graphql_name='degree')

    details = sgqlc.types.Field('LocalizedString', graphql_name='details')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    location = sgqlc.types.Field('LocalizedString', graphql_name='location')

    school = sgqlc.types.Field('LocalizedString', graphql_name='school')

    year = sgqlc.types.Field(Int, graphql_name='year')



class Experimental_SelfVerifiedEducationConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_SelfVerifiedEducationEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_SelfVerifiedEducationEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(Experimental_SelfVerifiedEducation), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_SelfVerifiedReference(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('contact', 'id', 'name', 'relationship')
    contact = sgqlc.types.Field(String, graphql_name='contact')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field('LocalizedString', graphql_name='name')

    relationship = sgqlc.types.Field('LocalizedString', graphql_name='relationship')



class Experimental_SelfVerifiedReferenceConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_SelfVerifiedReferenceEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_SelfVerifiedReferenceEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(Experimental_SelfVerifiedReference), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_SelfVerifiedTraining(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('details', 'id', 'instructor', 'location', 'school', 'training', 'year')
    details = sgqlc.types.Field('LocalizedString', graphql_name='details')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    instructor = sgqlc.types.Field('LocalizedString', graphql_name='instructor')

    location = sgqlc.types.Field('LocalizedString', graphql_name='location')

    school = sgqlc.types.Field('LocalizedString', graphql_name='school')

    training = sgqlc.types.Field('LocalizedString', graphql_name='training')

    year = sgqlc.types.Field(Int, graphql_name='year')



class Experimental_SelfVerifiedTrainingConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_SelfVerifiedTrainingEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Experimental_SelfVerifiedTrainingEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(Experimental_SelfVerifiedTraining), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_StringConstraint(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('error_message', 'value')
    error_message = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='errorMessage')

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')



class Experimental_TextFormElementConstraints(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_required', 'max_length', 'min_length', 'pattern')
    is_required = sgqlc.types.Field(Experimental_BooleanConstraint, graphql_name='isRequired')

    max_length = sgqlc.types.Field(Experimental_IntThresholdConstraint, graphql_name='maxLength')

    min_length = sgqlc.types.Field(Experimental_IntThresholdConstraint, graphql_name='minLength')

    pattern = sgqlc.types.Field(Experimental_StringConstraint, graphql_name='pattern')



class Experimental_TitleCoreCatalogResponse(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('keywords',)
    keywords = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Experimental_KeywordItem)), graphql_name='keywords')



class Experimental_TrackNotificationPreferences(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_tracking', 'notification_preferences')
    is_tracking = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTracking')

    notification_preferences = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Experimental_NotificationPreference)), graphql_name='notificationPreferences')



class Experimental_UIWorkflow(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('body', 'content_header', 'context_header', 'footer', 'global_menu', 'workflow_state', 'workflow_type')
    body = sgqlc.types.Field(sgqlc.types.non_null('Experimental_UIWorkflowBody'), graphql_name='body')

    content_header = sgqlc.types.Field(sgqlc.types.non_null('Experimental_UIWorkflowContentHeader'), graphql_name='contentHeader')

    context_header = sgqlc.types.Field(sgqlc.types.non_null('Experimental_UIWorkflowContextHeader'), graphql_name='contextHeader')

    footer = sgqlc.types.Field(sgqlc.types.non_null('Experimental_UIWorkflowFooter'), graphql_name='footer')

    global_menu = sgqlc.types.Field('Experimental_UIWorkflowGlobalMenu', graphql_name='globalMenu')

    workflow_state = sgqlc.types.Field(sgqlc.types.non_null('Experimental_UIWorkflowExecutionState'), graphql_name='workflowState')

    workflow_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowType), graphql_name='workflowType')



class Experimental_UIWorkflowAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('action_type', 'id', 'label')
    action_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowActionType), graphql_name='actionType')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    label = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='label')



class Experimental_UIWorkflowBody(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('elements',)
    elements = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_UIWorkflowElement'))), graphql_name='elements')



class Experimental_UIWorkflowCTA(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('start_workflow_action_context', 'workflow_type')
    start_workflow_action_context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='startWorkflowActionContext')

    workflow_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowType), graphql_name='workflowType')



class Experimental_UIWorkflowContentHeader(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('actions', 'description', 'heading', 'subheading')
    actions = sgqlc.types.Field('Experimental_UIWorkflowContentHeaderActions', graphql_name='actions')

    description = sgqlc.types.Field('LocalizedMarkdown', graphql_name='description')

    heading = sgqlc.types.Field('LocalizedMarkdown', graphql_name='heading')

    subheading = sgqlc.types.Field('LocalizedMarkdown', graphql_name='subheading')



class Experimental_UIWorkflowContentHeaderActions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('add_item_action',)
    add_item_action = sgqlc.types.Field('Experimental_UIWorkflowItemAction', graphql_name='addItemAction')



class Experimental_UIWorkflowContextHeader(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('heading', 'subject')
    heading = sgqlc.types.Field('LocalizedMarkdown', graphql_name='heading')

    subject = sgqlc.types.Field(sgqlc.types.non_null('Experimental_UIWorkflowSubject'), graphql_name='subject')



class Experimental_UIWorkflowExecutionState(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('execution_id', 'interaction_id', 'status', 'workflow_id')
    execution_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='executionId')

    interaction_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='interactionId')

    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')

    workflow_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workflowId')



class Experimental_UIWorkflowFeedbackDisplayElement(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('feedback_type', 'help_link', 'id', 'messages')
    feedback_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowFeedbackType), graphql_name='feedbackType')

    help_link = sgqlc.types.Field('Experimental_UIWorkflowHelpLink', graphql_name='helpLink')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LocalizedMarkdown'))), graphql_name='messages')



class Experimental_UIWorkflowFooter(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('actions', 'footer')
    actions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Experimental_UIWorkflowAction))), graphql_name='actions')

    footer = sgqlc.types.Field('LocalizedMarkdown', graphql_name='footer')



class Experimental_UIWorkflowGlobalMenu(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('menu_items',)
    menu_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Experimental_UIWorkflowGlobalMenuItem'))), graphql_name='menuItems')



class Experimental_UIWorkflowGlobalMenuItemLink(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('link_type', 'text', 'url')
    link_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowGlobalMenuItemLinkType), graphql_name='linkType')

    text = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='text')

    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')



class Experimental_UIWorkflowHelpLink(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('text', 'url')
    text = sgqlc.types.Field(sgqlc.types.non_null('LocalizedString'), graphql_name='text')

    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')



class Experimental_UIWorkflowItemAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('action_type', 'id', 'label')
    action_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowItemActionType), graphql_name='actionType')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    label = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='label')



class Experimental_UIWorkflowMarkdownDisplayElement(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'markdown')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    markdown = sgqlc.types.Field(sgqlc.types.non_null('LocalizedMarkdown'), graphql_name='markdown')



class Experimental_UIWorkflowNewSubject(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('type',)
    type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowSubjectType), graphql_name='type')



class Experimental_UploadDestination(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('expiration', 'upload_url')
    expiration = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='expiration')

    upload_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='uploadUrl')



class ExportStatus(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(ExportStatusId, graphql_name='id')

    name = sgqlc.types.Field('ExportStatusName', graphql_name='name')



class ExternalLinkCategoryWithExternalLinks(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'external_links', 'restriction')
    category = sgqlc.types.Field('ExternalLinkCategory', graphql_name='category')

    external_links = sgqlc.types.Field('ExternalLinkConnection', graphql_name='externalLinks', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    restriction = sgqlc.types.Field('ExternalLinkRestriction', graphql_name='restriction')



class ExternalLinkCategoryWithFeaturedExternalLinks(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('external_links', 'featured_category')
    external_links = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ExternalLink'))), graphql_name='externalLinks')

    featured_category = sgqlc.types.Field(sgqlc.types.non_null('ExternalLinkCategory'), graphql_name='featuredCategory')



class Faq(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('answer', 'experimental_edit_call_to_action', 'id', 'is_spoiler', 'language', 'question')
    answer = sgqlc.types.Field('Markdown', graphql_name='answer')

    experimental_edit_call_to_action = sgqlc.types.Field(Experimental_UIWorkflowCTA, graphql_name='experimental_editCallToAction')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_spoiler = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSpoiler')

    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')

    question = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='question')



class FeedbackGiven(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('has_given_feedback',)
    has_given_feedback = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasGivenFeedback')



class FilmLengths(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FilmLength'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class FilmingDates(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('date_range',)
    date_range = sgqlc.types.Field(DisplayableDateRange, graphql_name='dateRange')



class FollowerStatistics(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('displayable_count', 'total_count')
    displayable_count = sgqlc.types.Field(sgqlc.types.non_null('LocalizedDisplayableCount'), graphql_name='displayableCount')

    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')



class GenreSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('genre', 'total')
    genre = sgqlc.types.Field(sgqlc.types.non_null('GenreItem'), graphql_name='genre')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class GoofCategoryWithGoofs(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'goofs')
    category = sgqlc.types.Field(sgqlc.types.non_null('GoofCategory'), graphql_name='category')

    goofs = sgqlc.types.Field('GoofConnection', graphql_name='goofs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(GoofCategoryWithGoofsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `filter` (`GoofCategoryWithGoofsFilter`)None
    * `first` (`Int`)None
    '''



class GranularDirective(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('allow', 'id')
    allow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allow')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class GuildAffiliationEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null('GuildAffiliationVerificationStatus'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class GuildAffiliationVerificationStatus(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('company', 'is_verified_by_guild')
    company = sgqlc.types.Field(sgqlc.types.non_null('Company'), graphql_name='company')

    is_verified_by_guild = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerifiedByGuild')



class GuildAffiliationVisibilitiesConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GuildAffiliationVisibilitiesEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class GuildAffiliationVisibilitiesEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null('GuildAffiliationVisibilityStatus'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class GuildAffiliationVisibilityStatus(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('company', 'visibility')
    company = sgqlc.types.Field(sgqlc.types.non_null('Company'), graphql_name='company')

    visibility = sgqlc.types.Field(sgqlc.types.non_null(GuildAffiliationVisibilityLevel), graphql_name='visibility')



class GuildAffiliationsConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GuildAffiliationEdge))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class GuildMembershipDetail(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('company', 'membership_id')
    company = sgqlc.types.Field(sgqlc.types.non_null('Company'), graphql_name='company')

    membership_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='membershipId')



class GuildStatus(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_actra_apprentice', 'is_non_union', 'is_sag_eligible')
    is_actra_apprentice = sgqlc.types.Field(Boolean, graphql_name='isActraApprentice')

    is_non_union = sgqlc.types.Field(Boolean, graphql_name='isNonUnion')

    is_sag_eligible = sgqlc.types.Field(Boolean, graphql_name='isSagEligible')



class Histogram(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('demographic', 'histogram_values')
    demographic = sgqlc.types.Field(sgqlc.types.non_null(Demographic), graphql_name='demographic')

    histogram_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('HistogramValues')), graphql_name='histogramValues')



class HistogramValues(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('rating', 'vote_count')
    rating = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rating')

    vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='voteCount')



class ImageAndLinkCallToAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('action', 'background_image', 'result_id')
    action = sgqlc.types.Field(sgqlc.types.non_null(ActionLink), graphql_name='action')

    background_image = sgqlc.types.Field('CallToActionImage', graphql_name='backgroundImage')

    result_id = sgqlc.types.Field(sgqlc.types.non_null(ResultID), graphql_name='resultId')



class ImageEditParameters(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('crop_box', 'rotation')
    crop_box = sgqlc.types.Field(CroppingParameters, graphql_name='cropBox')

    rotation = sgqlc.types.Field(Float, graphql_name='rotation')



class ImageFacets(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('galleries', 'names', 'titles', 'types')
    galleries = sgqlc.types.Field('ImageGalleryFacetConnection', graphql_name='galleries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    names = sgqlc.types.Field('NameFacetConnection', graphql_name='names', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    titles = sgqlc.types.Field('TitleFacetConnection', graphql_name='titles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ImageTypeFacet')), graphql_name='types', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class ImageGallery(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('gallery_text', 'id', 'images')
    gallery_text = sgqlc.types.Field(String, graphql_name='galleryText')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    images = sgqlc.types.Field('ImageConnection', graphql_name='images', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('bust', sgqlc.types.Arg(String, graphql_name='bust', default=None)),
        ('filter', sgqlc.types.Arg(ImagesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `bust` (`String`)None
    * `filter` (`ImagesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''



class ImageTypeFacet(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('total', 'type')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')

    type = sgqlc.types.Field(sgqlc.types.non_null('ImageType'), graphql_name='type')



class ImageTypeWithImages(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('image_type', 'images')
    image_type = sgqlc.types.Field(sgqlc.types.non_null('ImageType'), graphql_name='imageType')

    images = sgqlc.types.Field('ImageTypesConnection', graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class Interest(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'description', 'engagement_statistics', 'id', 'primary_image', 'primary_text', 'score', 'secondary_text', 'similar_interests', 'visibility_level')
    category = sgqlc.types.Field('InterestCategory', graphql_name='category')

    description = sgqlc.types.Field('LocalizedMarkdown', graphql_name='description')

    engagement_statistics = sgqlc.types.Field(EngagementStatistics, graphql_name='engagementStatistics')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    primary_image = sgqlc.types.Field('Image', graphql_name='primaryImage')

    primary_text = sgqlc.types.Field('InterestText', graphql_name='primaryText')

    score = sgqlc.types.Field('InterestImportanceScore', graphql_name='score')

    secondary_text = sgqlc.types.Field('InterestText', graphql_name='secondaryText')

    similar_interests = sgqlc.types.Field('InterestConnection', graphql_name='similarInterests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    visibility_level = sgqlc.types.Field(InterestVisibilityLevel, graphql_name='visibilityLevel')



class InterestScore(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('users_interested', 'users_voted')
    users_interested = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usersInterested')

    users_voted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usersVoted')



class IsElementInList(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_element_in_list', 'item_element_id', 'item_ids')
    is_element_in_list = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isElementInList')

    item_element_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemElementId')

    item_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='itemIds')



class Keyword(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'id', 'text', 'titles')
    category = sgqlc.types.Field('KeywordCategory', graphql_name='category')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    text = sgqlc.types.Field('KeywordText', graphql_name='text')

    titles = sgqlc.types.Field('KeywordTitleConnection', graphql_name='titles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''



class KeywordCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class KeywordMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('keyword_categories',)
    keyword_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(KeywordCategory))), graphql_name='keywordCategories', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class Laboratories(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Laboratory'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class LengthMeasurement(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('unit', 'value')
    unit = sgqlc.types.Field(LengthUnit, graphql_name='unit')

    value = sgqlc.types.Field(Float, graphql_name='value')



class LinkCallToAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('action', 'result_id')
    action = sgqlc.types.Field(sgqlc.types.non_null(ActionLink), graphql_name='action')

    result_id = sgqlc.types.Field(sgqlc.types.non_null(ResultID), graphql_name='resultId')



class LinkedAuthProvider(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('deprecation_message', 'type')
    deprecation_message = sgqlc.types.Field(AuthProviderDeprecationMessage, graphql_name='deprecationMessage')

    type = sgqlc.types.Field(sgqlc.types.non_null(AuthProviderType), graphql_name='type')



class List(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('are_elements_in_list', 'author', 'created_date', 'description', 'id', 'is_element_in_list', 'is_predefined', 'items', 'last_modified_date', 'list_class', 'list_interaction_counts', 'list_type', 'name', 'name_list_item_search', 'primary_image', 'title_list_item_search', 'visibility')
    are_elements_in_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IsElementInList)), graphql_name='areElementsInList', args=sgqlc.types.ArgDict((
        ('item_element_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='itemElementIds', default=None)),
))
    )
    '''Arguments:

    * `item_element_ids` (`[ID!]!`)None
    '''

    author = sgqlc.types.Field('UserProfile', graphql_name='author')

    created_date = sgqlc.types.Field(DateTime, graphql_name='createdDate')

    description = sgqlc.types.Field('ListDescription', graphql_name='description')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_element_in_list = sgqlc.types.Field(Boolean, graphql_name='isElementInList', args=sgqlc.types.ArgDict((
        ('item_element_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='itemElementId', default=None)),
))
    )
    '''Arguments:

    * `item_element_id` (`ID!`)None
    '''

    is_predefined = sgqlc.types.Field(Boolean, graphql_name='isPredefined')

    items = sgqlc.types.Field('ListConnection', graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ListItemFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('jump_to_position', sgqlc.types.Arg(Int, graphql_name='jumpToPosition', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(ListItemSort, graphql_name='sort', default={'by': 'LIST_ORDER', 'order': 'ASC'})),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ListItemFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `jump_to_position` (`Int`)None
    * `last` (`Int`)None
    * `sort` (`ListItemSort`)None (default: `{by: LIST_ORDER, order:
      ASC}`)
    '''

    last_modified_date = sgqlc.types.Field(DateTime, graphql_name='lastModifiedDate')

    list_class = sgqlc.types.Field('ListClass', graphql_name='listClass')

    list_interaction_counts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ListInteractionCounts')), graphql_name='listInteractionCounts', args=sgqlc.types.ArgDict((
        ('time_ranges', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ListInteractionCountTimeRange))), graphql_name='timeRanges', default=None)),
))
    )
    '''Arguments:

    * `time_ranges` (`[ListInteractionCountTimeRange!]!`)None
    '''

    list_type = sgqlc.types.Field('ListType', graphql_name='listType')

    name = sgqlc.types.Field('ListName', graphql_name='name')

    name_list_item_search = sgqlc.types.Field('NameListItemSearchConnection', graphql_name='nameListItemSearch', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(AdvancedNameSearchConstraints, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(NameListSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `filter` (`AdvancedNameSearchConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`NameListSearchSort`)None
    '''

    primary_image = sgqlc.types.Field('ListPrimaryImage', graphql_name='primaryImage')

    title_list_item_search = sgqlc.types.Field('TitleListItemSearchConnection', graphql_name='titleListItemSearch', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(AdvancedTitleSearchConstraints, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(TitleListSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `filter` (`AdvancedTitleSearchConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`TitleListSearchSort`)None
    '''

    visibility = sgqlc.types.Field('ListVisibility', graphql_name='visibility')



class ListClass(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ListClassId), graphql_name='id')

    name = sgqlc.types.Field('ListClassName', graphql_name='name')



class ListCollectionConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ListCollectionEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ListCollectionEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(List), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ListDescription(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('original_text',)
    original_text = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='originalText')



class ListFieldAttributeMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('list_description', 'list_item_description', 'list_name')
    list_description = sgqlc.types.Field(sgqlc.types.non_null('ListTextFieldMetadata'), graphql_name='listDescription')

    list_item_description = sgqlc.types.Field(sgqlc.types.non_null('ListTextFieldMetadata'), graphql_name='listItemDescription')

    list_name = sgqlc.types.Field(sgqlc.types.non_null('ListTextFieldMetadata'), graphql_name='listName')



class ListInteractionCounts(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('clicks', 'list_id', 'time_range', 'views')
    clicks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='clicks')

    list_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='listId')

    time_range = sgqlc.types.Field(sgqlc.types.non_null(ListInteractionCountTimeRange), graphql_name='timeRange')

    views = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='views')



class ListItemNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('created_date', 'description', 'item_id', 'last_modified_date', 'list_item')
    created_date = sgqlc.types.Field(DateTime, graphql_name='createdDate')

    description = sgqlc.types.Field(ListDescription, graphql_name='description')

    item_id = sgqlc.types.Field(ID, graphql_name='itemId')

    last_modified_date = sgqlc.types.Field(DateTime, graphql_name='lastModifiedDate')

    list_item = sgqlc.types.Field('ListItem', graphql_name='listItem')



class ListItemSearchNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('created_date', 'description', 'item_id', 'last_modified_date')
    created_date = sgqlc.types.Field(DateTime, graphql_name='createdDate')

    description = sgqlc.types.Field(ListDescription, graphql_name='description')

    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')

    last_modified_date = sgqlc.types.Field(DateTime, graphql_name='lastModifiedDate')



class ListName(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('original_text',)
    original_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='originalText')



class ListPrimaryImage(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('image',)
    image = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='image')



class ListTextFieldMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('max_characters',)
    max_characters = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxCharacters')



class ListType(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ListTypeId), graphql_name='id')



class ListVisibility(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(ListVisibilityId, graphql_name='id')

    name = sgqlc.types.Field('ListVisibilityName', graphql_name='name')



class LocalizedMarkdown(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('language', 'value')
    language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='language')

    value = sgqlc.types.Field(sgqlc.types.non_null('Markdown'), graphql_name='value')



class LocalizedString(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('language', 'value')
    language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='language')

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')



class MainSearchNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('entity', 'id')
    entity = sgqlc.types.Field(sgqlc.types.non_null('MainSearchEntity'), graphql_name='entity')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class ManagedClient(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('client', 'status')
    client = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='client')

    status = sgqlc.types.Field(sgqlc.types.non_null(ManagedClientStatus), graphql_name='status')



class ManagedCompanyData(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('known_for',)
    known_for = sgqlc.types.Field('ManagedCompanyKnownForGroup', graphql_name='knownFor')



class ManagedCompanyKeyStaffGroup(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('automatic', 'automatic_history', 'custom', 'custom_history', 'source_preference')
    automatic = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKeyStaffCategory'), graphql_name='automatic')

    automatic_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKeyStaffHistory'), graphql_name='automaticHistory')

    custom = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKeyStaffCategory'), graphql_name='custom')

    custom_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKeyStaffHistory'), graphql_name='customHistory')

    source_preference = sgqlc.types.Field(sgqlc.types.non_null(KnownForPreference), graphql_name='sourcePreference')



class ManagedCompanyKeyStaffHistory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('key_staff_history',)
    key_staff_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKeyStaffHistoryConnection'), graphql_name='keyStaffHistory', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKnownForClientGroup(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('automatic', 'automatic_history', 'custom', 'custom_history', 'source_preference')
    automatic = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForClientCategory'), graphql_name='automatic')

    automatic_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForClientHistory'), graphql_name='automaticHistory')

    custom = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForClientCategory'), graphql_name='custom')

    custom_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForClientHistory'), graphql_name='customHistory')

    source_preference = sgqlc.types.Field(sgqlc.types.non_null(KnownForPreference), graphql_name='sourcePreference')



class ManagedCompanyKnownForClientHistory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('client_history',)
    client_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForClientHistoryConnection'), graphql_name='clientHistory', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKnownForGroup(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('key_staff', 'known_for_client', 'known_for_title')
    key_staff = sgqlc.types.Field(sgqlc.types.non_null(ManagedCompanyKeyStaffGroup), graphql_name='keyStaff')

    known_for_client = sgqlc.types.Field(sgqlc.types.non_null(ManagedCompanyKnownForClientGroup), graphql_name='knownForClient')

    known_for_title = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleGroup'), graphql_name='knownForTitle')



class ManagedCompanyKnownForTitleGroup(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('automatic', 'automatic_history', 'custom', 'custom_history', 'source_preference')
    automatic = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleCategory'), graphql_name='automatic')

    automatic_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleHistory'), graphql_name='automaticHistory')

    custom = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleCategory'), graphql_name='custom')

    custom_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleHistory'), graphql_name='customHistory')

    source_preference = sgqlc.types.Field(sgqlc.types.non_null(KnownForPreference), graphql_name='sourcePreference')



class ManagedCompanyKnownForTitleHistory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title_history',)
    title_history = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleHistoryConnection'), graphql_name='titleHistory', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagingRepresentative(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('manager', 'status')
    manager = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='manager')

    status = sgqlc.types.Field(sgqlc.types.non_null(ManagingRepresentativeStatus), graphql_name='status')



class Markdown(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('expanded_markdown', 'markdown', 'plaid_html', 'plain_text', 'related_entities')
    expanded_markdown = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expandedMarkdown', args=sgqlc.types.ArgDict((
        ('show_original_title_text', sgqlc.types.Arg(Boolean, graphql_name='showOriginalTitleText', default=None)),
))
    )
    '''Arguments:

    * `show_original_title_text` (`Boolean`)None
    '''

    markdown = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='markdown')

    plaid_html = sgqlc.types.Field(String, graphql_name='plaidHtml', args=sgqlc.types.ArgDict((
        ('query_params', sgqlc.types.Arg(String, graphql_name='queryParams', default=None)),
        ('show_line_break', sgqlc.types.Arg(Boolean, graphql_name='showLineBreak', default=None)),
        ('show_original_title_text', sgqlc.types.Arg(Boolean, graphql_name='showOriginalTitleText', default=None)),
))
    )
    '''Arguments:

    * `query_params` (`String`)None
    * `show_line_break` (`Boolean`)None
    * `show_original_title_text` (`Boolean`)None
    '''

    plain_text = sgqlc.types.Field(String, graphql_name='plainText', args=sgqlc.types.ArgDict((
        ('show_original_title_text', sgqlc.types.Arg(Boolean, graphql_name='showOriginalTitleText', default=None)),
))
    )
    '''Arguments:

    * `show_original_title_text` (`Boolean`)None
    '''

    related_entities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarkdownEntity')), graphql_name='relatedEntities', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    '''



class MarkdownSlotCallToAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('markdown', 'result_id')
    markdown = sgqlc.types.Field(LocalizedMarkdown, graphql_name='markdown')

    result_id = sgqlc.types.Field(sgqlc.types.non_null(ResultID), graphql_name='resultId')



class Metacritic(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('metascore', 'reviews', 'url')
    metascore = sgqlc.types.Field(sgqlc.types.non_null('Metascore'), graphql_name='metascore')

    reviews = sgqlc.types.Field('MetacriticReviewConnection', graphql_name='reviews', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    url = sgqlc.types.Field(URL, graphql_name='url')



class MetacriticReview(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('quote', 'reviewer', 'score', 'site', 'url')
    quote = sgqlc.types.Field(LocalizedString, graphql_name='quote')

    reviewer = sgqlc.types.Field(String, graphql_name='reviewer')

    score = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='score')

    site = sgqlc.types.Field(String, graphql_name='site')

    url = sgqlc.types.Field(URL, graphql_name='url')



class Metascore(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('review_count', 'score')
    review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='reviewCount')

    score = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='score')



class MeterEvent(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title', 'type')
    title = sgqlc.types.Field('Title', graphql_name='title')

    type = sgqlc.types.Field(LocalizedString, graphql_name='type')



class MeterRankChange(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('change_direction', 'difference')
    change_direction = sgqlc.types.Field(sgqlc.types.non_null(MeterRankChangeDirection), graphql_name='changeDirection')

    difference = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='difference')



class MeterRankingHistoryEntry(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('date', 'events', 'rank')
    date = sgqlc.types.Field(Date, graphql_name='date')

    events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MeterEvent)), graphql_name='events')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')



class ModifiedBy(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('role',)
    role = sgqlc.types.Field(sgqlc.types.non_null(UserRole), graphql_name='role')



class Money(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('amount', 'currency')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='amount')

    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currency')



class MoreLikeThisConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MoreLikeThisEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')



class MoreLikeThisEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class MoreLikeThisNameConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MoreLikeThisNameEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')



class MoreLikeThisNameEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cursor', 'node', 'position')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class MultiLinkCallToAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('abbreviated_actions', 'result_id', 'standard_actions')
    abbreviated_actions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NamedActionLink')), graphql_name='abbreviatedActions')

    result_id = sgqlc.types.Field(sgqlc.types.non_null(ResultID), graphql_name='resultId')

    standard_actions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NamedActionLink')), graphql_name='standardActions')



class NameChartRankingsConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges',)
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NameChartRankingsEdge'))), graphql_name='edges')



class NameChartRankingsEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('NameChartRankingsNode'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameChartRankingsNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('item', 'rank')
    item = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='item')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')



class NameCreditCategoryWithCredits(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'credits')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    credits = sgqlc.types.Field('NameCreditConnection', graphql_name='credits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class NameCreditSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('categories', 'genres', 'title_type_categories', 'title_types', 'total_credits')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreditCategorySummary)), graphql_name='categories')

    genres = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GenreSummary)), graphql_name='genres')

    title_type_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TitleTypeCategorySummary')), graphql_name='titleTypeCategories')

    title_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TitleTypeSummary')), graphql_name='titleTypes')

    total_credits = sgqlc.types.Field('TotalCredits', graphql_name='totalCredits')



class NameDisplayPreferences(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('akas', 'awards', 'biography', 'height')
    akas = sgqlc.types.Field(sgqlc.types.non_null(NameDisplayVisibilityLevel), graphql_name='akas')

    awards = sgqlc.types.Field(sgqlc.types.non_null(NameDisplayVisibilityLevel), graphql_name='awards')

    biography = sgqlc.types.Field(sgqlc.types.non_null(NameDisplayVisibilityLevel), graphql_name='biography')

    height = sgqlc.types.Field(sgqlc.types.non_null(NameDisplayVisibilityLevel), graphql_name='height')



class NameKnownFor(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('credit', 'title')
    credit = sgqlc.types.Field(sgqlc.types.non_null(Credit), graphql_name='credit')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class NameManagedData(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('automatic_featured_images', 'automatic_known_for', 'automatic_primary_professions', 'custom_featured_images', 'custom_known_for', 'custom_primary_image', 'custom_primary_professions', 'display_preferences', 'latest_primary_image', 'managed_clients', 'managing_representatives')
    automatic_featured_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Image')), graphql_name='automaticFeaturedImages', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    '''

    automatic_known_for = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Title')), graphql_name='automaticKnownFor', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    '''

    automatic_primary_professions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PrimaryProfession')), graphql_name='automaticPrimaryProfessions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    custom_featured_images = sgqlc.types.Field(CustomFeaturedImages, graphql_name='customFeaturedImages')

    custom_known_for = sgqlc.types.Field(CustomKnownFor, graphql_name='customKnownFor')

    custom_primary_image = sgqlc.types.Field(CustomPrimaryImage, graphql_name='customPrimaryImage')

    custom_primary_professions = sgqlc.types.Field(CustomPrimaryProfessions, graphql_name='customPrimaryProfessions')

    display_preferences = sgqlc.types.Field(NameDisplayPreferences, graphql_name='displayPreferences')

    latest_primary_image = sgqlc.types.Field('Image', graphql_name='latestPrimaryImage')

    managed_clients = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ManagedClient)), graphql_name='managedClients', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    managing_representatives = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ManagingRepresentative)), graphql_name='managingRepresentatives', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''



class NameManagingPermissionRequestResponse(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_valid', 'requester', 'target')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')

    requester = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='requester')

    target = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='target')



class NameMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name_credit_categories',)
    name_credit_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NameCreditCategory'))), graphql_name='nameCreditCategories')



class NamePersonalLocationMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('limit', 'valid_values')
    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')

    valid_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamePersonalLocation'))), graphql_name='validValues')



class NamePersonalLocations(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('locations', 'total')
    locations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamePersonalLocation'))), graphql_name='locations')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameProfession(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'profession', 'profession_category', 'short_description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    profession = sgqlc.types.Field(sgqlc.types.non_null('DisplayableProfession'), graphql_name='profession')

    profession_category = sgqlc.types.Field(sgqlc.types.non_null('ProfessionCategory'), graphql_name='professionCategory')

    short_description = sgqlc.types.Field('DisplayableProfessionDescription', graphql_name='shortDescription')



class NameRecommendation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('explanation', 'name')
    explanation = sgqlc.types.Field(sgqlc.types.non_null(LocalizedMarkdown), graphql_name='explanation')

    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')



class NameRecommendations(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('names', 'ref_tag')
    names = sgqlc.types.Field('NameRecommendationConnection', graphql_name='names', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    ref_tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTag')



class NameRelation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('birth_date', 'gender_identity', 'id', 'relation_name', 'relationship_type')
    birth_date = sgqlc.types.Field('DisplayableDate', graphql_name='birthDate')

    gender_identity = sgqlc.types.Field('GenderIdentity', graphql_name='genderIdentity')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    relation_name = sgqlc.types.Field('RelationName', graphql_name='relationName')

    relationship_type = sgqlc.types.Field(sgqlc.types.non_null('NameRelationType'), graphql_name='relationshipType')



class NameSearchIndexing(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('disable_indexing',)
    disable_indexing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableIndexing')



class NameText(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class NameToTitleAttachment(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('attachment_time', 'character_list', 'credit_categories', 'id', 'name', 'title')
    attachment_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='attachmentTime')

    character_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='characterList')

    credit_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreditCategory'))), graphql_name='creditCategories')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class NameWeight(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('unit', 'value')
    unit = sgqlc.types.Field(sgqlc.types.non_null(WeightUnit), graphql_name='unit')

    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')



class NamedActionLink(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('action_name', 'label', 'url')
    action_name = sgqlc.types.Field(sgqlc.types.non_null(ActionLinkName), graphql_name='actionName')

    label = sgqlc.types.Field(CallToActionText, graphql_name='label')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')



class NegativeFormats(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NegativeFormat'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class News(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('article_title', 'byline', 'date', 'external_url', 'id', 'image', 'language', 'source', 'text')
    article_title = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='articleTitle')

    byline = sgqlc.types.Field(String, graphql_name='byline')

    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')

    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    image = sgqlc.types.Field('Image', graphql_name='image')

    language = sgqlc.types.Field('DisplayableLanguage', graphql_name='language')

    source = sgqlc.types.Field(sgqlc.types.non_null('NewsSource'), graphql_name='source')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class NewsConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'restriction', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NewsEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('NewsPageInfo'), graphql_name='pageInfo')

    restriction = sgqlc.types.Field('NewsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NewsEdge(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(News), graphql_name='node')



class NewsPageInfo(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('end_cursor', 'has_next_page')
    end_cursor = sgqlc.types.Field(ID, graphql_name='endCursor')

    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')



class NewsSource(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('description', 'homepage', 'icon', 'id', 'trusted_source')
    description = sgqlc.types.Field(String, graphql_name='description')

    homepage = sgqlc.types.Field('NewsLink', graphql_name='homepage')

    icon = sgqlc.types.Field('NewsSourceIconImage', graphql_name='icon')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    trusted_source = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='trustedSource')



class Nomination(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award', 'awarded_entities', 'category', 'event', 'event_edition', 'for_episodes', 'for_song_titles', 'id', 'is_winner', 'notes', 'win_announcement_date', 'winning_rank')
    award = sgqlc.types.Field('NominationAward', graphql_name='award')

    awarded_entities = sgqlc.types.Field('AwardedEntities', graphql_name='awardedEntities')

    category = sgqlc.types.Field(AwardCategory, graphql_name='category')

    event = sgqlc.types.Field('NominationEvent', graphql_name='event')

    event_edition = sgqlc.types.Field('NominationEventEdition', graphql_name='eventEdition')

    for_episodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Title')), graphql_name='forEpisodes')

    for_song_titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DisplayableSongTitle')), graphql_name='forSongTitles')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_winner = sgqlc.types.Field(Boolean, graphql_name='isWinner')

    notes = sgqlc.types.Field(Markdown, graphql_name='notes')

    win_announcement_date = sgqlc.types.Field('DisplayableDate', graphql_name='winAnnouncementDate')

    winning_rank = sgqlc.types.Field(Int, graphql_name='winningRank')



class NominationEvent(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('awards', 'editions', 'id', 'location', 'name', 'trivia', 'urls')
    awards = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NominationAward'))), graphql_name='awards', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    editions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NominationEventEdition'))), graphql_name='editions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    location = sgqlc.types.Field('DisplayableLocation', graphql_name='location')

    name = sgqlc.types.Field(sgqlc.types.non_null('NominationEventName'), graphql_name='name')

    trivia = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Markdown))), graphql_name='trivia', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EventUrl))), graphql_name='urls', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class NominationEventEdition(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('awards', 'event', 'id', 'instance_within_year', 'trivia', 'year')
    awards = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NominationAward'))), graphql_name='awards', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    event = sgqlc.types.Field(sgqlc.types.non_null(NominationEvent), graphql_name='event')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    instance_within_year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instanceWithinYear')

    trivia = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Markdown))), graphql_name='trivia', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')



class NominationsWithCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'nominations')
    category = sgqlc.types.Field(AwardCategory, graphql_name='category')

    nominations = sgqlc.types.Field('NominationConnection', graphql_name='nominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(NominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`NominationsSort`)None
    '''



class OpeningWeekendGross(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('box_office_area_type', 'gross', 'theater_count', 'weekend_end_date', 'weekend_start_date')
    box_office_area_type = sgqlc.types.Field(sgqlc.types.non_null('BoxOfficeAreaType'), graphql_name='boxOfficeAreaType')

    gross = sgqlc.types.Field(sgqlc.types.non_null(BoxOfficeGross), graphql_name='gross')

    theater_count = sgqlc.types.Field(Int, graphql_name='theaterCount')

    weekend_end_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='weekendEndDate')

    weekend_start_date = sgqlc.types.Field(Date, graphql_name='weekendStartDate')



class PageInfo(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor')
    end_cursor = sgqlc.types.Field(ID, graphql_name='endCursor')

    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')

    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')

    start_cursor = sgqlc.types.Field(ID, graphql_name='startCursor')



class PaginatedTitles(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('pagination_token', 'titles')
    pagination_token = sgqlc.types.Field(String, graphql_name='paginationToken')

    titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Title'))), graphql_name='titles')



class PaginatedVideos(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('pagination_token', 'videos')
    pagination_token = sgqlc.types.Field(String, graphql_name='paginationToken')

    videos = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Video')), graphql_name='videos')



class ParentsGuide(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('categories', 'guide_items')
    categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ParentsGuideCategorySummary')), graphql_name='categories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ParentsGuideCategoryFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`ParentsGuideCategoryFilter`)None
    '''

    guide_items = sgqlc.types.Field('ParentsGuideConnection', graphql_name='guideItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ParentsGuideFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ParentsGuideFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''



class ParentsGuideCategorySummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'guide_items', 'severity', 'severity_breakdown', 'total_severity_votes')
    category = sgqlc.types.Field(sgqlc.types.non_null('ParentsGuideCategory'), graphql_name='category')

    guide_items = sgqlc.types.Field('ParentsGuideConnection', graphql_name='guideItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    severity = sgqlc.types.Field('SeverityLevel', graphql_name='severity')

    severity_breakdown = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SeverityLevel')), graphql_name='severityBreakdown')

    total_severity_votes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalSeverityVotes')



class ParentsGuideItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'correction_link', 'id', 'is_spoiler', 'reporting_link', 'text', 'title')
    category = sgqlc.types.Field(sgqlc.types.non_null('ParentsGuideCategory'), graphql_name='category')

    correction_link = sgqlc.types.Field(ContributionLink, graphql_name='correctionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_spoiler = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSpoiler')

    reporting_link = sgqlc.types.Field(ContributionLink, graphql_name='reportingLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')

    title = sgqlc.types.Field('Title', graphql_name='title')



class PlaybackURL(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('display_name', 'url', 'video_definition', 'video_mime_type')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='displayName')

    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')

    video_definition = sgqlc.types.Field(sgqlc.types.non_null(VideoDefinition), graphql_name='videoDefinition')

    video_mime_type = sgqlc.types.Field(sgqlc.types.non_null(VideoMimeType), graphql_name='videoMimeType')



class Plot(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('author', 'correction_link', 'id', 'is_spoiler', 'language', 'plot_text', 'plot_type', 'reporting_link', 'restriction', 'title')
    author = sgqlc.types.Field(String, graphql_name='author')

    correction_link = sgqlc.types.Field(ContributionLink, graphql_name='correctionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_spoiler = sgqlc.types.Field(Boolean, graphql_name='isSpoiler')

    language = sgqlc.types.Field('DisplayableLanguage', graphql_name='language')

    plot_text = sgqlc.types.Field(Markdown, graphql_name='plotText')

    plot_type = sgqlc.types.Field(PlotType, graphql_name='plotType')

    reporting_link = sgqlc.types.Field(ContributionLink, graphql_name='reportingLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    restriction = sgqlc.types.Field('PlotRestriction', graphql_name='restriction')

    title = sgqlc.types.Field('Title', graphql_name='title')



class Poll(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('answers', 'id', 'primary_image', 'question')
    answers = sgqlc.types.Field('PollAnswersConnection', graphql_name='answers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    primary_image = sgqlc.types.Field('PollPrimaryImage', graphql_name='primaryImage')

    question = sgqlc.types.Field('PollQuestion', graphql_name='question')



class PollAnswer(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('item',)
    item = sgqlc.types.Field(sgqlc.types.non_null('AnswerItem'), graphql_name='item')



class PollPrimaryImage(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('image',)
    image = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='image')



class PollQuestion(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('original_text',)
    original_text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='originalText')



class PrestigiousAwardSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('award_nomination', 'nominations', 'wins')
    award_nomination = sgqlc.types.Field(sgqlc.types.non_null(AwardNomination), graphql_name='awardNomination')

    nominations = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nominations')

    wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='wins')



class PrimaryProfession(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'profession')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    profession = sgqlc.types.Field('Profession', graphql_name='profession')



class PrimaryWatchOption(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('additional_watch_options_count', 'watch_option')
    additional_watch_options_count = sgqlc.types.Field(Int, graphql_name='additionalWatchOptionsCount')

    watch_option = sgqlc.types.Field(sgqlc.types.non_null('WatchOption'), graphql_name='watchOption')



class PrincipalCreditsForCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'credits', 'restriction', 'total_credits')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    credits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Credit))), graphql_name='credits', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    restriction = sgqlc.types.Field('CreditRestriction', graphql_name='restriction')

    total_credits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCredits')



class PrintedFormats(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PrintedFormat'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class PrivacyDirectives(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('avl_tcf_string', 'cross_use_string', 'directives_cookie', 'expiration_date', 'gvl_tcf_string', 'purposes', 'vendors')
    avl_tcf_string = sgqlc.types.Field(String, graphql_name='avlTcfString')

    cross_use_string = sgqlc.types.Field(String, graphql_name='crossUseString')

    directives_cookie = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='directivesCookie')

    expiration_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='expirationDate')

    gvl_tcf_string = sgqlc.types.Field(String, graphql_name='gvlTcfString')

    purposes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GranularDirective)), graphql_name='purposes')

    vendors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GranularDirective)), graphql_name='vendors')



class PrivacyDirectivesOutput(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('directives',)
    directives = sgqlc.types.Field(PrivacyDirectives, graphql_name='directives')



class PrivacyPrompt(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('customize_url', 'id', 'prompt_markdown', 'show_prompt_on_page_load')
    customize_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='customizeUrl')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    prompt_markdown = sgqlc.types.Field(sgqlc.types.non_null(LocalizedMarkdown), graphql_name='promptMarkdown')

    show_prompt_on_page_load = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showPromptOnPageLoad')



class PrivacyPromptOutput(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('expiration_date', 'privacy_prompt')
    expiration_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='expirationDate')

    privacy_prompt = sgqlc.types.Field(PrivacyPrompt, graphql_name='privacyPrompt')



class ProStatus(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('has_subscription',)
    has_subscription = sgqlc.types.Field(Boolean, graphql_name='hasSubscription')



class Processes(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Process'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ProductionAnnouncement(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('comment', 'date')
    comment = sgqlc.types.Field('ProductionAnnouncementComment', graphql_name='comment')

    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')



class ProductionBudget(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('budget',)
    budget = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='budget')



class ProductionDate(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('attributes', 'end_date', 'start_date')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute)), graphql_name='attributes')

    end_date = sgqlc.types.Field('DisplayableDate', graphql_name='endDate')

    start_date = sgqlc.types.Field('DisplayableDate', graphql_name='startDate')



class ProductionStatusDetails(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('announcements', 'current_production_stage', 'production_status_history', 'restriction')
    announcements = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionAnnouncement)), graphql_name='announcements')

    current_production_stage = sgqlc.types.Field(sgqlc.types.non_null('ProductionStage'), graphql_name='currentProductionStage')

    production_status_history = sgqlc.types.Field(sgqlc.types.list_of('ProductionStatusHistory'), graphql_name='productionStatusHistory')

    restriction = sgqlc.types.Field('ProductionStatusHistoryRestriction', graphql_name='restriction')



class ProductionStatusHistory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('comment', 'date', 'stage', 'status')
    comment = sgqlc.types.Field('ProductionStatusHistoryComment', graphql_name='comment')

    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')

    stage = sgqlc.types.Field(sgqlc.types.non_null('ProductionStage'), graphql_name='stage')

    status = sgqlc.types.Field(sgqlc.types.non_null('ProductionStatus'), graphql_name='status')



class ProfessionCategory(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'linked_credit_category', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    linked_credit_category = sgqlc.types.Field('CreditCategory', graphql_name='linkedCreditCategory')

    text = sgqlc.types.Field(sgqlc.types.non_null('DisplayableProfessionCategory'), graphql_name='text')



class PromotedVideoAd(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('ad_feedback_url', 'id', 'third_party_trackers', 'video')
    ad_feedback_url = sgqlc.types.Field(URL, graphql_name='adFeedbackUrl')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    third_party_trackers = sgqlc.types.Field(sgqlc.types.non_null('ThirdPartyTrackers'), graphql_name='thirdPartyTrackers')

    video = sgqlc.types.Field(sgqlc.types.non_null('Video'), graphql_name='video')



class PublicityCategoryWithListings(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'publicity_listings')
    category = sgqlc.types.Field(sgqlc.types.non_null('PublicityListingCategory'), graphql_name='category')

    publicity_listings = sgqlc.types.Field('PublicityListingConnection', graphql_name='publicityListings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class PushNotificationUserSettings(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('push_notification_user_id',)
    push_notification_user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pushNotificationUserId')



class Query(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('_polls_workaround', 'advanced_name_search', 'advanced_title_search', 'born_today', 'box_office_weekend_chart', 'call_to_action', 'can_claim_name_page', 'chart_names', 'chart_titles', 'claimed_name', 'coming_soon', 'companies', 'company', 'company_metadata', 'contribution_questions', 'contributor_leaderboards', 'contributor_rankings', 'display_ads_for_app', 'displayable_prompt', 'event_live_results', 'event_metadata', 'experimental_nomination', 'experimental_nomination_event', 'experimental_nomination_event_edition', 'experimental_nomination_event_editions', 'experimental_nomination_events', 'experimental_nominations', 'experimental_get_latest_uiworkflow', 'experimental_media_upload_destination', 'experimental_obi_wan', 'experimental_title_core_catalog_query', 'fan_picks_titles', 'get_exports', 'guild_membership_detail', 'image', 'image_galleries', 'image_gallery', 'images', 'interest', 'interest_categories', 'interests', 'keyword', 'keyword_metadata', 'keywords', 'latest_name_to_title_attachments', 'list', 'list_field_attribute_metadata', 'lists', 'main_search', 'name', 'name_chart_rankings', 'name_managing_permission_request', 'name_metadata', 'name_recommendations', 'names', 'news', 'news_article', 'news_source', 'nomination', 'nomination_event', 'nomination_event_edition', 'nomination_event_editions', 'nomination_events', 'nominations', 'outstream_video_ad_app', 'popular_interests', 'popular_titles', 'predefined_list', 'privacy_directives', 'privacy_prompt', 'profession', 'profession_categories', 'profession_category', 'profession_name_track_recommendations', 'profession_title_track_recommendations', 'professions', 'promoted_video_ad', 'push_notification_user_settings', 'recent_videos', 'recently_viewed_items', 'related_news', 'rendered_markdown', 'review', 'search_metadata', 'self_verified_name_metadata', 'showtimes_titles', 'showtimes_titles_by_cinemas', 'similar_name_track_recommendations', 'similar_title_track_recommendations', 'streaming_titles', 'stub_query', 'suggestion_search', 'symphony_placements', 'test', 'test_auth', 'test_auth_timer', 'test_combined_entitlement', 'test_context_entitlement', 'test_entitlement', 'test_entitlements', 'test_pro_any_tier_entitlement', 'test_pro_premium_entitlement', 'title', 'title_chart_rankings', 'title_genre_recommendations', 'title_metadata', 'title_recommendations', 'title_watchlist_recommendations', 'titles', 'top_grossing_releases', 'top_lists_for_item', 'top_meter_names', 'top_meter_titles', 'top_picks_titles', 'top_trending_names', 'top_trending_sets_predefined', 'top_trending_titles', 'top_trending_videos', 'tracked_names', 'tracked_titles', 'trending_names_collection_options', 'trending_titles', 'trending_titles_collection_options', 'unreleased_title_track_recommendations', 'user', 'user_consent', 'user_list_search', 'user_profile_by_user_id', 'user_ratings', 'user_reviews', 'vanity_url', 'video', 'video_ad_feedback_url', 'video_recommendations', 'videos', 'watch_providers')
    _polls_workaround = sgqlc.types.Field(String, graphql_name='_pollsWorkaround')

    advanced_name_search = sgqlc.types.Field('AdvancedNameSearchConnection', graphql_name='advancedNameSearch', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('constraints', sgqlc.types.Arg(AdvancedNameSearchConstraints, graphql_name='constraints', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(AdvancedNameSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `constraints` (`AdvancedNameSearchConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`AdvancedNameSearchSort`)None
    '''

    advanced_title_search = sgqlc.types.Field('AdvancedTitleSearchConnection', graphql_name='advancedTitleSearch', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('constraints', sgqlc.types.Arg(AdvancedTitleSearchConstraints, graphql_name='constraints', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(AdvancedTitleSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `constraints` (`AdvancedTitleSearchConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`AdvancedTitleSearchSort`)None
    '''

    born_today = sgqlc.types.Field('NameSearchConnection', graphql_name='bornToday', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('today', sgqlc.types.Arg(sgqlc.types.non_null(MonthDay), graphql_name='today', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    * `today` (`MonthDay!`)None
    '''

    box_office_weekend_chart = sgqlc.types.Field(BoxOfficeWeekendChart, graphql_name='boxOfficeWeekendChart', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    call_to_action = sgqlc.types.Field(CallToAction, graphql_name='callToAction', args=sgqlc.types.ArgDict((
        ('context', sgqlc.types.Arg(CallToActionContextInput, graphql_name='context', default=None)),
))
    )
    '''Arguments:

    * `context` (`CallToActionContextInput`)None
    '''

    can_claim_name_page = sgqlc.types.Field(Boolean, graphql_name='canClaimNamePage')

    chart_names = sgqlc.types.Field('ChartNameSearchConnection', graphql_name='chartNames', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('chart', sgqlc.types.Arg(sgqlc.types.non_null(ChartNameOptions), graphql_name='chart', default=None)),
        ('filter', sgqlc.types.Arg(AdvancedNameSearchConstraints, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(AdvancedNameSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `chart` (`ChartNameOptions!`)None
    * `filter` (`AdvancedNameSearchConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`AdvancedNameSearchSort`)None
    '''

    chart_titles = sgqlc.types.Field('ChartTitleSearchConnection', graphql_name='chartTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('chart', sgqlc.types.Arg(sgqlc.types.non_null(ChartTitleOptions), graphql_name='chart', default=None)),
        ('filter', sgqlc.types.Arg(AdvancedTitleSearchConstraints, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(AdvancedTitleSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `chart` (`ChartTitleOptions!`)None
    * `filter` (`AdvancedTitleSearchConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`AdvancedTitleSearchSort`)None
    '''

    claimed_name = sgqlc.types.Field(ClaimedName, graphql_name='claimedName')

    coming_soon = sgqlc.types.Field('TitleSearchConnection', graphql_name='comingSoon', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('coming_soon_type', sgqlc.types.Arg(sgqlc.types.non_null(ComingSoonType), graphql_name='comingSoonType', default=None)),
        ('disable_popularity_filter', sgqlc.types.Arg(Boolean, graphql_name='disablePopularityFilter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('region_override', sgqlc.types.Arg(String, graphql_name='regionOverride', default=None)),
        ('releasing_on_or_after', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='releasingOnOrAfter', default=None)),
        ('releasing_on_or_before', sgqlc.types.Arg(Date, graphql_name='releasingOnOrBefore', default=None)),
        ('sort', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ComingSoonSort)), graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `coming_soon_type` (`ComingSoonType!`)None
    * `disable_popularity_filter` (`Boolean`)None
    * `first` (`Int!`)None
    * `region_override` (`String`)None
    * `releasing_on_or_after` (`Date!`)None
    * `releasing_on_or_before` (`Date`)None
    * `sort` (`[ComingSoonSort!]`)None
    '''

    companies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Company')), graphql_name='companies', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]`)None
    '''

    company = sgqlc.types.Field('Company', graphql_name='company', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    company_metadata = sgqlc.types.Field(CompanyMetadata, graphql_name='companyMetadata')

    contribution_questions = sgqlc.types.Field('QuestionConnection', graphql_name='contributionQuestions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(QuestionsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('pinned_question', sgqlc.types.Arg(String, graphql_name='pinnedQuestion', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`QuestionsFilter`)None
    * `first` (`Int`)None
    * `pinned_question` (`String`)None
    '''

    contributor_leaderboards = sgqlc.types.Field(ContributorLeaderboards, graphql_name='contributorLeaderboards')

    contributor_rankings = sgqlc.types.Field(sgqlc.types.non_null('ContributorLeaderboardRankConnection'), graphql_name='contributorRankings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ContributorRankingsFilter), graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ContributorRankingsFilter!`)None
    * `first` (`Int`)None
    '''

    display_ads_for_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AdSlot)), graphql_name='displayAdsForApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DisplayAdsForAppInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`DisplayAdsForAppInput!`)None
    '''

    displayable_prompt = sgqlc.types.Field(sgqlc.types.non_null(DisplayablePrompt), graphql_name='displayablePrompt', args=sgqlc.types.ArgDict((
        ('const_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='constId', default=None)),
        ('prompt_type', sgqlc.types.Arg(sgqlc.types.non_null(PromptType), graphql_name='promptType', default=None)),
))
    )
    '''Arguments:

    * `const_id` (`ID!`)None
    * `prompt_type` (`PromptType!`)None
    '''

    event_live_results = sgqlc.types.Field(EventLiveResults, graphql_name='eventLiveResults', args=sgqlc.types.ArgDict((
        ('override', sgqlc.types.Arg(EventLiveResultsOverrideInput, graphql_name='override', default=None)),
))
    )
    '''Arguments:

    * `override` (`EventLiveResultsOverrideInput`)None
    '''

    event_metadata = sgqlc.types.Field(EventMetadata, graphql_name='eventMetadata')

    experimental_nomination = sgqlc.types.Field(ExperimentalNomination, graphql_name='experimentalNomination', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    experimental_nomination_event = sgqlc.types.Field(ExperimentalNominationEvent, graphql_name='experimentalNominationEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    experimental_nomination_event_edition = sgqlc.types.Field(ExperimentalNominationEventEdition, graphql_name='experimentalNominationEventEdition', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    experimental_nomination_event_editions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ExperimentalNominationEventEdition)), graphql_name='experimentalNominationEventEditions', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`[ID!]`)None
    '''

    experimental_nomination_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ExperimentalNominationEvent)), graphql_name='experimentalNominationEvents', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]`)None
    '''

    experimental_nominations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ExperimentalNomination)), graphql_name='experimentalNominations', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`[ID!]`)None
    '''

    experimental_get_latest_uiworkflow = sgqlc.types.Field(Experimental_UIWorkflow, graphql_name='experimental_getLatestUIWorkflow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(Experimental_GetLatestUIWorkflowInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`Experimental_GetLatestUIWorkflowInput!`)None
    '''

    experimental_media_upload_destination = sgqlc.types.Field(Experimental_MediaUploadDestination, graphql_name='experimental_mediaUploadDestination', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(Experimental_UploadDestinationInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`Experimental_UploadDestinationInput!`)None
    '''

    experimental_obi_wan = sgqlc.types.Field(Experimental_Kenobi, graphql_name='experimental_obiWan')

    experimental_title_core_catalog_query = sgqlc.types.Field(Experimental_TitleCoreCatalogResponse, graphql_name='experimental_titleCoreCatalogQuery', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(Experimental_CatalogQueryInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`Experimental_CatalogQueryInput!`)None
    '''

    fan_picks_titles = sgqlc.types.Field('FanPicksConnection', graphql_name='fanPicksTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(FanPicksFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`FanPicksFilter`)None
    * `first` (`Int!`)None
    '''

    get_exports = sgqlc.types.Field(sgqlc.types.non_null('ExportDetailConnection'), graphql_name='getExports', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(ExportFilterByInput, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GetExportsInput), graphql_name='input', default=None)),
        ('sort', sgqlc.types.Arg(ExportSortByInput, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ExportFilterByInput`)None
    * `first` (`Int!`)None
    * `input` (`GetExportsInput!`)None
    * `sort` (`ExportSortByInput`)None
    '''

    guild_membership_detail = sgqlc.types.Field(GuildMembershipDetail, graphql_name='guildMembershipDetail', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='companyId', default=None)),
))
    )
    '''Arguments:

    * `company_id` (`ID!`)None
    '''

    image = sgqlc.types.Field('Image', graphql_name='image', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    image_galleries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ImageGallery)), graphql_name='imageGalleries', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    image_gallery = sgqlc.types.Field(ImageGallery, graphql_name='imageGallery', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    images = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Image')), graphql_name='images', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    interest = sgqlc.types.Field(Interest, graphql_name='interest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    interest_categories = sgqlc.types.Field('InterestCategoryConnection', graphql_name='interestCategories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(InterestCategoriesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`InterestCategoriesFilter`)None
    * `first` (`Int!`)None
    '''

    interests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Interest)), graphql_name='interests', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    keyword = sgqlc.types.Field(Keyword, graphql_name='keyword', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    keyword_metadata = sgqlc.types.Field(KeywordMetadata, graphql_name='keywordMetadata')

    keywords = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Keyword)), graphql_name='keywords', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]`)None
    '''

    latest_name_to_title_attachments = sgqlc.types.Field('NameToTitleAttachmentConnection', graphql_name='latestNameToTitleAttachments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('attachment_constraint', sgqlc.types.Arg(AttachmentSearchConstraint, graphql_name='attachmentConstraint', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `attachment_constraint` (`AttachmentSearchConstraint`)None
    * `first` (`Int!`)None
    '''

    list = sgqlc.types.Field(List, graphql_name='list', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    list_field_attribute_metadata = sgqlc.types.Field(sgqlc.types.non_null(ListFieldAttributeMetadata), graphql_name='listFieldAttributeMetadata')

    lists = sgqlc.types.Field(sgqlc.types.non_null(ListCollectionConnection), graphql_name='lists', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ListFilter), graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('list_owner_user_id', sgqlc.types.Arg(ID, graphql_name='listOwnerUserId', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ListFilter!`)None
    * `first` (`Int!`)None
    * `list_owner_user_id` (`ID`)None
    '''

    main_search = sgqlc.types.Field('MainSearchConnection', graphql_name='mainSearch', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('options', sgqlc.types.Arg(sgqlc.types.non_null(MainSearchOptions), graphql_name='options', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int!`)None
    * `options` (`MainSearchOptions!`)None
    '''

    name = sgqlc.types.Field('Name', graphql_name='name', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    name_chart_rankings = sgqlc.types.Field(NameChartRankingsConnection, graphql_name='nameChartRankings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NameChartRankingsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    * `input` (`NameChartRankingsInput!`)None
    '''

    name_managing_permission_request = sgqlc.types.Field(NameManagingPermissionRequestResponse, graphql_name='nameManagingPermissionRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='token', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    * `token` (`String!`)None
    '''

    name_metadata = sgqlc.types.Field(NameMetadata, graphql_name='nameMetadata')

    name_recommendations = sgqlc.types.Field(NameRecommendations, graphql_name='nameRecommendations')

    names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Name')), graphql_name='names', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    news = sgqlc.types.Field(NewsConnection, graphql_name='news', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('category', sgqlc.types.Arg(sgqlc.types.non_null(NewsCategory), graphql_name='category', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `category` (`NewsCategory!`)None
    * `first` (`Int!`)None
    '''

    news_article = sgqlc.types.Field(News, graphql_name='newsArticle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    news_source = sgqlc.types.Field(NewsSource, graphql_name='newsSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    nomination = sgqlc.types.Field(Nomination, graphql_name='nomination', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    nomination_event = sgqlc.types.Field(NominationEvent, graphql_name='nominationEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    nomination_event_edition = sgqlc.types.Field(NominationEventEdition, graphql_name='nominationEventEdition', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    nomination_event_editions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NominationEventEdition)), graphql_name='nominationEventEditions', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    nomination_events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NominationEvent)), graphql_name='nominationEvents', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    nominations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Nomination)), graphql_name='nominations', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    outstream_video_ad_app = sgqlc.types.Field(URL, graphql_name='outstreamVideoAdApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OutstreamAdParametersApp), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`OutstreamAdParametersApp!`)None
    '''

    popular_interests = sgqlc.types.Field('InterestSearchConnection', graphql_name='popularInterests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int!`)None
    '''

    popular_titles = sgqlc.types.Field(PaginatedTitles, graphql_name='popularTitles', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
        ('pagination_token', sgqlc.types.Arg(String, graphql_name='paginationToken', default=None)),
        ('query_filter', sgqlc.types.Arg(PopularTitlesQueryFilter, graphql_name='queryFilter', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    * `pagination_token` (`String`)None
    * `query_filter` (`PopularTitlesQueryFilter`)None
    '''

    predefined_list = sgqlc.types.Field(List, graphql_name='predefinedList', args=sgqlc.types.ArgDict((
        ('class_type', sgqlc.types.Arg(sgqlc.types.non_null(ListClassId), graphql_name='classType', default=None)),
        ('user_id', sgqlc.types.Arg(ID, graphql_name='userId', default=None)),
))
    )
    '''Arguments:

    * `class_type` (`ListClassId!`)None
    * `user_id` (`ID`)None
    '''

    privacy_directives = sgqlc.types.Field(sgqlc.types.non_null(PrivacyDirectivesOutput), graphql_name='privacyDirectives')

    privacy_prompt = sgqlc.types.Field(sgqlc.types.non_null(PrivacyPromptOutput), graphql_name='privacyPrompt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PrivacyPromptInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`PrivacyPromptInput!`)None
    '''

    profession = sgqlc.types.Field(NameProfession, graphql_name='profession', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    profession_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProfessionCategory))), graphql_name='professionCategories', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    profession_category = sgqlc.types.Field(ProfessionCategory, graphql_name='professionCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    profession_name_track_recommendations = sgqlc.types.Field('NameTrackRecommendationsConnection', graphql_name='professionNameTrackRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TrackRecommendationsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    * `input` (`TrackRecommendationsInput!`)None
    '''

    profession_title_track_recommendations = sgqlc.types.Field('TitleTrackRecommendationsConnection', graphql_name='professionTitleTrackRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TrackRecommendationsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    * `input` (`TrackRecommendationsInput!`)None
    '''

    professions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NameProfession))), graphql_name='professions', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    promoted_video_ad = sgqlc.types.Field(PromotedVideoAd, graphql_name='promotedVideoAd', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PromotedVideoAdParameters), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`PromotedVideoAdParameters!`)None
    '''

    push_notification_user_settings = sgqlc.types.Field(PushNotificationUserSettings, graphql_name='pushNotificationUserSettings')

    recent_videos = sgqlc.types.Field(PaginatedVideos, graphql_name='recentVideos', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
        ('pagination_token', sgqlc.types.Arg(String, graphql_name='paginationToken', default=None)),
        ('query_filter', sgqlc.types.Arg(RecentVideosQueryFilter, graphql_name='queryFilter', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    * `pagination_token` (`String`)None
    * `query_filter` (`RecentVideosQueryFilter`)None
    '''

    recently_viewed_items = sgqlc.types.Field('RecentlyViewedConnection', graphql_name='recentlyViewedItems', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    related_news = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelatedNews')), graphql_name='relatedNews', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    rendered_markdown = sgqlc.types.Field(Markdown, graphql_name='renderedMarkdown', args=sgqlc.types.ArgDict((
        ('markdown_string', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='markdownString', default=None)),
))
    )
    '''Arguments:

    * `markdown_string` (`String!`)None
    '''

    review = sgqlc.types.Field('Review', graphql_name='review', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    search_metadata = sgqlc.types.Field('SearchMetadata', graphql_name='searchMetadata')

    self_verified_name_metadata = sgqlc.types.Field('SelfVerifiedNameMetadata', graphql_name='selfVerifiedNameMetadata')

    showtimes_titles = sgqlc.types.Field('ShowtimesTitleConnection', graphql_name='showtimesTitles', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('location', sgqlc.types.Arg(sgqlc.types.non_null(ShowtimesLocation), graphql_name='location', default=None)),
        ('query_metadata', sgqlc.types.Arg(sgqlc.types.non_null(ShowtimesTitlesQueryMetadata), graphql_name='queryMetadata', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    * `location` (`ShowtimesLocation!`)None
    * `query_metadata` (`ShowtimesTitlesQueryMetadata!`)None
    '''

    showtimes_titles_by_cinemas = sgqlc.types.Field('ShowtimesTitleConnection', graphql_name='showtimesTitlesByCinemas', args=sgqlc.types.ArgDict((
        ('cinemas_metadata', sgqlc.types.Arg(sgqlc.types.non_null(ShowtimesTitlesCinemasMetadata), graphql_name='cinemasMetadata', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `cinemas_metadata` (`ShowtimesTitlesCinemasMetadata!`)None
    * `first` (`Int`)None
    '''

    similar_name_track_recommendations = sgqlc.types.Field('NameTrackRecommendationsConnection', graphql_name='similarNameTrackRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    similar_title_track_recommendations = sgqlc.types.Field('TitleTrackRecommendationsConnection', graphql_name='similarTitleTrackRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    streaming_titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StreamingTitles'))), graphql_name='streamingTitles', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(StreamingTitlesFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`StreamingTitlesFilter`)None
    '''

    stub_query = sgqlc.types.Field('QueryStubs', graphql_name='stubQuery')

    suggestion_search = sgqlc.types.Field('SuggestionSearchConnection', graphql_name='suggestionSearch', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SuggestionSearchFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('search_term', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='searchTerm', default=None)),
        ('should_show_original_titles', sgqlc.types.Arg(Boolean, graphql_name='shouldShowOriginalTitles', default=None)),
))
    )
    '''Arguments:

    * `filter` (`SuggestionSearchFilter`)None
    * `first` (`Int!`)None
    * `search_term` (`String!`)None
    * `should_show_original_titles` (`Boolean`)None
    '''

    symphony_placements = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SymphonyPlacement')), graphql_name='symphonyPlacements', args=sgqlc.types.ArgDict((
        ('cached', sgqlc.types.Arg(Boolean, graphql_name='cached', default=False)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GetPlacementsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `cached` (`Boolean`)None (default: `false`)
    * `input` (`GetPlacementsInput!`)None
    '''

    test = sgqlc.types.Field('Test', graphql_name='test')

    test_auth = sgqlc.types.Field('TestAuth', graphql_name='testAuth')

    test_auth_timer = sgqlc.types.Field('TestAuthTimer', graphql_name='testAuthTimer')

    test_combined_entitlement = sgqlc.types.Field(Boolean, graphql_name='testCombinedEntitlement')

    test_context_entitlement = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Boolean)), graphql_name='testContextEntitlement', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    test_entitlement = sgqlc.types.Field(Boolean, graphql_name='testEntitlement')

    test_entitlements = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TestEntitlement')), graphql_name='testEntitlements')

    test_pro_any_tier_entitlement = sgqlc.types.Field(Boolean, graphql_name='testProAnyTierEntitlement')

    test_pro_premium_entitlement = sgqlc.types.Field(Boolean, graphql_name='testProPremiumEntitlement')

    title = sgqlc.types.Field('Title', graphql_name='title', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    title_chart_rankings = sgqlc.types.Field('TitleChartRankingsConnection', graphql_name='titleChartRankings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TitleChartRankingsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    * `input` (`TitleChartRankingsInput!`)None
    '''

    title_genre_recommendations = sgqlc.types.Field('TitleGenreRecommendation', graphql_name='titleGenreRecommendations')

    title_metadata = sgqlc.types.Field('TitleMetadata', graphql_name='titleMetadata')

    title_recommendations = sgqlc.types.Field('TitleRecommendationConnection', graphql_name='titleRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(TitleRecommendationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('placement_context', sgqlc.types.Arg(PlacementContext, graphql_name='placementContext', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `filter` (`TitleRecommendationsFilter`)None
    * `first` (`Int!`)None
    * `placement_context` (`PlacementContext`)None
    '''

    title_watchlist_recommendations = sgqlc.types.Field('TitleWatchlistRecommendationConnection', graphql_name='titleWatchlistRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Title')), graphql_name='titles', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    top_grossing_releases = sgqlc.types.Field('TopGrossingReleasesConnection', graphql_name='topGrossingReleases', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TopGrossingReleasesFilter), graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`TopGrossingReleasesFilter!`)None
    * `first` (`Int!`)None
    '''

    top_lists_for_item = sgqlc.types.Field(sgqlc.types.non_null(ListCollectionConnection), graphql_name='topListsForItem', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='itemId', default=None)),
        ('top_list_type', sgqlc.types.Arg(sgqlc.types.non_null(TopListType), graphql_name='topListType', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    * `item_id` (`String!`)None
    * `top_list_type` (`TopListType!`)None
    '''

    top_meter_names = sgqlc.types.Field('NameSearchConnection', graphql_name='topMeterNames', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int!`)None
    '''

    top_meter_titles = sgqlc.types.Field('TitleSearchConnection', graphql_name='topMeterTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(TopMeterTitlesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `filter` (`TopMeterTitlesFilter`)None
    * `first` (`Int!`)None
    '''

    top_picks_titles = sgqlc.types.Field('TopPicksConnection', graphql_name='topPicksTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    top_trending_names = sgqlc.types.Field('TrendingNameConnection', graphql_name='topTrendingNames', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TopTrendingInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    * `input` (`TopTrendingInput!`)None
    '''

    top_trending_sets_predefined = sgqlc.types.Field('TrendingTitleConnection', graphql_name='topTrendingSetsPredefined', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TopTrendingSetsPredefinedInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    * `input` (`TopTrendingSetsPredefinedInput!`)None
    '''

    top_trending_titles = sgqlc.types.Field('TrendingTitleConnection', graphql_name='topTrendingTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TopTrendingInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    * `input` (`TopTrendingInput!`)None
    '''

    top_trending_videos = sgqlc.types.Field('TrendingVideoConnection', graphql_name='topTrendingVideos', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TopTrendingInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    * `input` (`TopTrendingInput!`)None
    '''

    tracked_names = sgqlc.types.Field('TrackedNamesConnection', graphql_name='trackedNames', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    tracked_titles = sgqlc.types.Field('TrackedTitlesConnection', graphql_name='trackedTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    trending_names_collection_options = sgqlc.types.Field('TrendingNameCollectionOptions', graphql_name='trendingNamesCollectionOptions')

    trending_titles = sgqlc.types.Field(PaginatedTitles, graphql_name='trendingTitles', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
        ('pagination_token', sgqlc.types.Arg(String, graphql_name='paginationToken', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int!`)None
    * `pagination_token` (`String`)None
    '''

    trending_titles_collection_options = sgqlc.types.Field('TrendingTitleCollectionOptions', graphql_name='trendingTitlesCollectionOptions')

    unreleased_title_track_recommendations = sgqlc.types.Field('TitleTrackRecommendationsConnection', graphql_name='unreleasedTitleTrackRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TrackRecommendationsInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    * `input` (`TrackRecommendationsInput!`)None
    '''

    user = sgqlc.types.Field('User', graphql_name='user')

    user_consent = sgqlc.types.Field('UserConsentOutput', graphql_name='userConsent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UserConsentInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UserConsentInput!`)None
    '''

    user_list_search = sgqlc.types.Field(sgqlc.types.non_null(ListCollectionConnection), graphql_name='userListSearch', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(ListSearchFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('list_owner_user_id', sgqlc.types.Arg(ID, graphql_name='listOwnerUserId', default=None)),
        ('sort', sgqlc.types.Arg(ListSearchSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ListSearchFilter`)None
    * `first` (`Int!`)None
    * `list_owner_user_id` (`ID`)None
    * `sort` (`ListSearchSort`)None
    '''

    user_profile_by_user_id = sgqlc.types.Field('UserProfile', graphql_name='userProfileByUserId', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='userId', default=None)),
))
    )
    '''Arguments:

    * `user_id` (`ID!`)None
    '''

    user_ratings = sgqlc.types.Field('RatingsConnection', graphql_name='userRatings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('constraints', sgqlc.types.Arg(RatingsConstraints, graphql_name='constraints', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(RatingsSort, graphql_name='sort', default=None)),
        ('user_id', sgqlc.types.Arg(ID, graphql_name='userId', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `constraints` (`RatingsConstraints`)None
    * `first` (`Int!`)None
    * `sort` (`RatingsSort`)None
    * `user_id` (`ID`)None
    '''

    user_reviews = sgqlc.types.Field(sgqlc.types.non_null('ReviewsConnection'), graphql_name='userReviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(UserReviewsInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int`)None
    * `input` (`UserReviewsInput`)None
    '''

    vanity_url = sgqlc.types.Field('VanityUrl', graphql_name='vanityUrl', args=sgqlc.types.ArgDict((
        ('url_path', sgqlc.types.Arg(String, graphql_name='urlPath', default=None)),
))
    )
    '''Arguments:

    * `url_path` (`String`)None
    '''

    video = sgqlc.types.Field('Video', graphql_name='video', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    video_ad_feedback_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='videoAdFeedbackUrl', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(VideoAdFeedbackUrlInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`VideoAdFeedbackUrlInput!`)None
    '''

    video_recommendations = sgqlc.types.Field('VideoRecommendationsConnection', graphql_name='videoRecommendations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('context', sgqlc.types.Arg(sgqlc.types.non_null(VideoRecommendationsContext), graphql_name='context', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `context` (`VideoRecommendationsContext!`)None
    * `first` (`Int!`)None
    '''

    videos = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Video')), graphql_name='videos', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    '''Arguments:

    * `ids` (`[ID!]!`)None
    '''

    watch_providers = sgqlc.types.Field('WatchProviderConnection', graphql_name='watchProviders', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(WatchProvidersQueryFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`WatchProvidersQueryFilter`)None
    * `first` (`Int!`)None
    '''



class QueryStubs(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('matrix',)
    matrix = sgqlc.types.Field('Title', graphql_name='matrix')



class Question(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('answer_options', 'answer_type', 'contribution_link', 'data_type', 'entity', 'entity_id', 'question_id', 'question_text')
    answer_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AnswerOption')), graphql_name='answerOptions')

    answer_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='answerType')

    contribution_link = sgqlc.types.Field(sgqlc.types.non_null(ContributionQuestionsLink), graphql_name='contributionLink')

    data_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dataType')

    entity = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='entity')

    entity_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entityId')

    question_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='questionId')

    question_text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='questionText')



class RankChange(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('change_direction', 'difference')
    change_direction = sgqlc.types.Field(sgqlc.types.non_null(RankChangeDirection), graphql_name='changeDirection')

    difference = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='difference')



class RankedLifetimeBoxOfficeGross(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('box_office_area_type', 'rank', 'total')
    box_office_area_type = sgqlc.types.Field(sgqlc.types.non_null('BoxOfficeAreaType'), graphql_name='boxOfficeAreaType')

    rank = sgqlc.types.Field(Int, graphql_name='rank')

    total = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='total')



class Rating(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('date', 'value')
    date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='date')

    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')



class RatingsResult(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title',)
    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class RatingsSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('aggregate_rating', 'notification_text', 'top_ranking', 'vote_count')
    aggregate_rating = sgqlc.types.Field(Float, graphql_name='aggregateRating')

    notification_text = sgqlc.types.Field(LocalizedMarkdown, graphql_name='notificationText')

    top_ranking = sgqlc.types.Field('TopRanking', graphql_name='topRanking')

    vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='voteCount')



class RatingsSummaryByCountry(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('aggregate', 'country', 'display_text', 'vote_count')
    aggregate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='aggregate')

    country = sgqlc.types.Field(sgqlc.types.non_null(Country), graphql_name='country')

    display_text = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='displayText')

    vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='voteCount')



class ReactionSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('count', 'display_count', 'reaction')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')

    display_count = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='displayCount')

    reaction = sgqlc.types.Field(sgqlc.types.non_null('Reaction'), graphql_name='reaction')



class ReactionSummaryGroup(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('aggregate_count', 'display_count', 'group_id', 'reaction_summaries', 'selection_type')
    aggregate_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='aggregateCount')

    display_count = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='displayCount')

    group_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='groupId')

    reaction_summaries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReactionSummary))), graphql_name='reactionSummaries')

    selection_type = sgqlc.types.Field(sgqlc.types.non_null(ReactionsGroupSelectionType), graphql_name='selectionType')



class ReactionsSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('reaction_summary_groups',)
    reaction_summary_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ReactionSummaryGroup))), graphql_name='reactionSummaryGroups')



class RecommendationExplanation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title',)
    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class RefTag(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('ep13n_reftag',)
    ep13n_reftag = sgqlc.types.Field(String, graphql_name='ep13nReftag')



class RelatedNews(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('entity', 'items')
    entity = sgqlc.types.Field(sgqlc.types.non_null('NewsEntity'), graphql_name='entity')

    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(News)), graphql_name='items')



class RestrictionExplanation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'reason', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    reason = sgqlc.types.Field(sgqlc.types.non_null(ContentRestrictionReason), graphql_name='reason')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class Review(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('author', 'author_rating', 'correction_link', 'deletion_link', 'helpfulness', 'id', 'language', 'reporting_link', 'spoiler', 'submission_date', 'summary', 'text', 'title')
    author = sgqlc.types.Field('UserProfile', graphql_name='author')

    author_rating = sgqlc.types.Field(Int, graphql_name='authorRating')

    correction_link = sgqlc.types.Field(ContributionLink, graphql_name='correctionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    deletion_link = sgqlc.types.Field(ContributionLink, graphql_name='deletionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    helpfulness = sgqlc.types.Field('ReviewHelpfulness', graphql_name='helpfulness')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    language = sgqlc.types.Field(Language, graphql_name='language')

    reporting_link = sgqlc.types.Field(ContributionLink, graphql_name='reportingLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    spoiler = sgqlc.types.Field(Boolean, graphql_name='spoiler')

    submission_date = sgqlc.types.Field(Date, graphql_name='submissionDate')

    summary = sgqlc.types.Field('ReviewSummary', graphql_name='summary')

    text = sgqlc.types.Field('ReviewText', graphql_name='text')

    title = sgqlc.types.Field('Title', graphql_name='title')



class ReviewHelpfulness(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('down_votes', 'score', 'up_votes')
    down_votes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downVotes')

    score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='score')

    up_votes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='upVotes')



class ReviewSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('original_text',)
    original_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='originalText')



class ReviewText(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('original_text',)
    original_text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='originalText')



class SearchAwardEventOptions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('events',)
    events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SearchAwardEvent'))), graphql_name='events')



class SearchMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('advanced_search_award_options',)
    advanced_search_award_options = sgqlc.types.Field(sgqlc.types.non_null(SearchAwardEventOptions), graphql_name='advancedSearchAwardOptions')



class SectionCallToAction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('action', 'result_id', 'section_content', 'section_title')
    action = sgqlc.types.Field(sgqlc.types.non_null(ActionLink), graphql_name='action')

    result_id = sgqlc.types.Field(sgqlc.types.non_null(ResultID), graphql_name='resultId')

    section_content = sgqlc.types.Field(CallToActionText, graphql_name='sectionContent')

    section_title = sgqlc.types.Field(CallToActionText, graphql_name='sectionTitle')



class SelfVerified(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('is_self_verified',)
    is_self_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSelfVerified')



class SelfVerifiedNameAttribute(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('total', 'values')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')

    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'))), graphql_name='values')



class SelfVerifiedNameAttributeMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('allow_free_form_text', 'limit', 'valid_values')
    allow_free_form_text = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowFreeFormText')

    limit = sgqlc.types.Field(Int, graphql_name='limit')

    valid_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SelfVerifiedNameAttributeValue')), graphql_name='validValues')



class SelfVerifiedNameAward(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('details', 'event', 'id', 'name', 'year')
    details = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='details')

    event = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='event')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='name')

    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')



class SelfVerifiedNameCredit(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('company_or_director', 'id', 'project_title', 'role_or_position', 'type')
    company_or_director = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='companyOrDirector')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    project_title = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='projectTitle')

    role_or_position = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='roleOrPosition')

    type = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameCreditType'), graphql_name='type')



class SelfVerifiedNameCreditMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('credit_types', 'limit')
    credit_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SelfVerifiedNameCreditType'))), graphql_name='creditTypes')

    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')



class SelfVerifiedNameCreditTypeWithCredits(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('credit_type', 'credits')
    credit_type = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameCreditType'), graphql_name='creditType')

    credits = sgqlc.types.Field('SelfVerifiedNameCreditConnection', graphql_name='credits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class SelfVerifiedNameData(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('accents', 'age_playing_range', 'athletic_skills', 'awards', 'blog', 'credit_types', 'dance_skills', 'educational_history', 'ethnic_appearances', 'eye_color', 'guild_affiliation_visibilities', 'guild_affiliations', 'guild_status', 'hair_color', 'hair_length', 'has_valid_passport', 'is_willing_to_work_unpaid', 'job_categories', 'job_titles', 'musical_instruments', 'performer_skills', 'personal_locations', 'physique', 'primary_citizenship', 'references', 'resume_custom_sections', 'resume_details', 'spoken_languages', 'trainings', 'twitter', 'unique_traits', 'voice_types', 'weight', 'work_authorization_countries', 'work_history_credit_types')
    accents = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='accents', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    age_playing_range = sgqlc.types.Field(AgePlayingRange, graphql_name='agePlayingRange')

    athletic_skills = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='athleticSkills', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    awards = sgqlc.types.Field('SelfVerifiedNameAwardConnection', graphql_name='awards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    blog = sgqlc.types.Field('BlogLink', graphql_name='blog')

    credit_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SelfVerifiedNameCreditTypeWithCredits)), graphql_name='creditTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SelfVerifiedNameCreditTypeFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`SelfVerifiedNameCreditTypeFilter`)None
    '''

    dance_skills = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='danceSkills', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    educational_history = sgqlc.types.Field('SelfVerifiedNameEducationalHistoryConnection', graphql_name='educationalHistory', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    ethnic_appearances = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='ethnicAppearances', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    eye_color = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='eyeColor')

    guild_affiliation_visibilities = sgqlc.types.Field(GuildAffiliationVisibilitiesConnection, graphql_name='guildAffiliationVisibilities', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(GuildAffiliationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`GuildAffiliationsFilter`)None
    * `first` (`Int!`)None
    '''

    guild_affiliations = sgqlc.types.Field(GuildAffiliationsConnection, graphql_name='guildAffiliations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(GuildAffiliationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`GuildAffiliationsFilter`)None
    * `first` (`Int!`)None
    '''

    guild_status = sgqlc.types.Field(GuildStatus, graphql_name='guildStatus')

    hair_color = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='hairColor')

    hair_length = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='hairLength')

    has_valid_passport = sgqlc.types.Field(Boolean, graphql_name='hasValidPassport')

    is_willing_to_work_unpaid = sgqlc.types.Field(Boolean, graphql_name='isWillingToWorkUnpaid')

    job_categories = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='jobCategories', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    job_titles = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='jobTitles', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    musical_instruments = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='musicalInstruments', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    performer_skills = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='performerSkills', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    personal_locations = sgqlc.types.Field(NamePersonalLocations, graphql_name='personalLocations', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    physique = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='physique')

    primary_citizenship = sgqlc.types.Field('LocalizedDisplayableCountry', graphql_name='primaryCitizenship')

    references = sgqlc.types.Field('SelfVerifiedNameReferenceConnection', graphql_name='references', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    resume_custom_sections = sgqlc.types.Field('SelfVerifiedResumeCustomSectionConnection', graphql_name='resumeCustomSections', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    resume_details = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='resumeDetails')

    spoken_languages = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='spokenLanguages', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    trainings = sgqlc.types.Field('SelfVerifiedNameTrainingConnection', graphql_name='trainings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    twitter = sgqlc.types.Field('TwitterLink', graphql_name='twitter')

    unique_traits = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='uniqueTraits', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    voice_types = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='voiceTypes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    weight = sgqlc.types.Field(NameWeight, graphql_name='weight', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(GetNameWeightInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`GetNameWeightInput`)None
    '''

    work_authorization_countries = sgqlc.types.Field('WorkAuthorizationCountries', graphql_name='workAuthorizationCountries', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    work_history_credit_types = sgqlc.types.Field(SelfVerifiedNameAttribute, graphql_name='workHistoryCreditTypes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class SelfVerifiedNameEducation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('degree', 'details', 'id', 'location', 'school', 'year')
    degree = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='degree')

    details = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='details')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    location = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='location')

    school = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='school')

    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')



class SelfVerifiedNameMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('accent', 'athletic_skill', 'award', 'credit', 'dance_skill', 'educational_history', 'ethnic_appearance', 'eye_color', 'guild_affiliation', 'hair_color', 'hair_length', 'job_category', 'job_title', 'musical_instrument', 'performer_skill', 'personal_location', 'physique', 'primary_citizenship', 'reference', 'resume_custom_section', 'spoken_language', 'training', 'unique_trait', 'voice_type', 'work_authorization_country', 'work_history_credit_type')
    accent = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='accent')

    athletic_skill = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='athleticSkill')

    award = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='award')

    credit = sgqlc.types.Field(SelfVerifiedNameCreditMetadata, graphql_name='credit')

    dance_skill = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='danceSkill')

    educational_history = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='educationalHistory')

    ethnic_appearance = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='ethnicAppearance')

    eye_color = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='eyeColor')

    guild_affiliation = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='guildAffiliation')

    hair_color = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='hairColor')

    hair_length = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='hairLength')

    job_category = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='jobCategory')

    job_title = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='jobTitle')

    musical_instrument = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='musicalInstrument')

    performer_skill = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='performerSkill')

    personal_location = sgqlc.types.Field(NamePersonalLocationMetadata, graphql_name='personalLocation')

    physique = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='physique')

    primary_citizenship = sgqlc.types.Field(CountryAttributeMetadata, graphql_name='primaryCitizenship')

    reference = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='reference')

    resume_custom_section = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='resumeCustomSection')

    spoken_language = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='spokenLanguage')

    training = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='training')

    unique_trait = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='uniqueTrait')

    voice_type = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='voiceType')

    work_authorization_country = sgqlc.types.Field(CountryAttributeMetadata, graphql_name='workAuthorizationCountry')

    work_history_credit_type = sgqlc.types.Field(SelfVerifiedNameAttributeMetadata, graphql_name='workHistoryCreditType')



class SelfVerifiedNameReference(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('contact_info', 'id', 'name', 'relationship')
    contact_info = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='contactInfo')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='name')

    relationship = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='relationship')



class SelfVerifiedNameTraining(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('details', 'id', 'instructor', 'location', 'school', 'type', 'year')
    details = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='details')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    instructor = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='instructor')

    location = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='location')

    school = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='school')

    type = sgqlc.types.Field('SelfVerifiedNameAttributeValue', graphql_name='type')

    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')



class SelfVerifiedNameTrainingConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('edges', 'page_info', 'total')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SelfVerifiedNameTrainingEdge'))), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SelfVerifiedResumeCustomSection(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('body', 'id', 'title')
    body = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='body')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    title = sgqlc.types.Field(sgqlc.types.non_null('SelfVerifiedNameAttributeValue'), graphql_name='title')



class Series(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('displayable_episode_number', 'next_episode', 'previous_episode', 'series')
    displayable_episode_number = sgqlc.types.Field(sgqlc.types.non_null(DisplayableEpisodeNumber), graphql_name='displayableEpisodeNumber')

    next_episode = sgqlc.types.Field('Title', graphql_name='nextEpisode')

    previous_episode = sgqlc.types.Field('Title', graphql_name='previousEpisode')

    series = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='series')



class SharedCreditCategorySummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('count', 'credit_category')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')

    credit_category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='creditCategory')



class SharedNameItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('descriptions', 'input_shared_titles', 'mutual_name', 'parent_shared_titles', 'score', 'total_input_shared_titles', 'total_parent_shared_titles')
    descriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConnectionDescription'))), graphql_name='descriptions')

    input_shared_titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Title'))), graphql_name='inputSharedTitles')

    mutual_name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='mutualName')

    parent_shared_titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Title'))), graphql_name='parentSharedTitles')

    score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='score')

    total_input_shared_titles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalInputSharedTitles')

    total_parent_shared_titles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalParentSharedTitles')



class SharedNamesResult(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('backfill_message', 'shared_credit_category_summary', 'shared_names')
    backfill_message = sgqlc.types.Field('BackfillMessage', graphql_name='backfillMessage')

    shared_credit_category_summary = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SharedCreditCategorySummary)), graphql_name='sharedCreditCategorySummary')

    shared_names = sgqlc.types.Field('SharedNamesConnection', graphql_name='sharedNames')



class Showtime(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'primary_ticketing', 'screening_start', 'screening_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    primary_ticketing = sgqlc.types.Field('ShowtimeTicketing', graphql_name='primaryTicketing')

    screening_start = sgqlc.types.Field(sgqlc.types.non_null('ScreeningDateTime'), graphql_name='screeningStart')

    screening_type = sgqlc.types.Field(sgqlc.types.non_null('ShowtimeScreeningType'), graphql_name='screeningType')



class ShowtimeTicketing(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='link')



class ShowtimesByScreeningType(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('screening_type', 'showtimes')
    screening_type = sgqlc.types.Field(sgqlc.types.non_null('ShowtimeScreeningType'), graphql_name='screeningType')

    showtimes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Showtime))), graphql_name='showtimes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class SoundMixes(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'restriction', 'total')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SoundMix'))), graphql_name='items')

    restriction = sgqlc.types.Field('TechnicalSpecificationsRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Source(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('attribution_url', 'banner', 'id', 'text')
    attribution_url = sgqlc.types.Field(String, graphql_name='attributionUrl')

    banner = sgqlc.types.Field('Banner', graphql_name='banner')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    text = sgqlc.types.Field(String, graphql_name='text')



class SpokenLanguages(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('language', 'spoken_languages')
    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')

    spoken_languages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SpokenLanguage'))), graphql_name='spokenLanguages', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''



class SpouseName(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('as_markdown', 'name')
    as_markdown = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='asMarkdown')

    name = sgqlc.types.Field('Name', graphql_name='name')



class StaffStatus(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category',)
    category = sgqlc.types.Field(sgqlc.types.non_null(StaffCategory), graphql_name='category')



class StreamingTitle(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('ref_tag', 'title')
    ref_tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTag')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class StreamingTitles(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('provider', 'titles')
    provider = sgqlc.types.Field('WatchProvider', graphql_name='provider')

    titles = sgqlc.types.Field('StreamingTitleConnection', graphql_name='titles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''



class SupportedQuestionFilters(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('countries', 'data_types', 'languages')
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='countries')

    data_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='dataTypes')

    languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='languages')



class SymphonyArgument(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')



class SymphonyMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('content_id', 'creative_id', 'multi_slot_group_name', 'multi_slot_order', 'placement_id')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')

    creative_id = sgqlc.types.Field(ID, graphql_name='creativeId')

    multi_slot_group_name = sgqlc.types.Field(String, graphql_name='multiSlotGroupName')

    multi_slot_order = sgqlc.types.Field(Int, graphql_name='multiSlotOrder')

    placement_id = sgqlc.types.Field(ID, graphql_name='placementId')



class SymphonyPlacement(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('component_arguments', 'component_metadata', 'component_name', 'slot')
    component_arguments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SymphonyArgument))), graphql_name='componentArguments')

    component_metadata = sgqlc.types.Field(SymphonyMetadata, graphql_name='componentMetadata')

    component_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='componentName')

    slot = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slot')



class TechnicalSpecifications(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('aspect_ratios', 'cameras', 'colorations', 'film_lengths', 'laboratories', 'negative_formats', 'printed_formats', 'processes', 'sound_mixes')
    aspect_ratios = sgqlc.types.Field(sgqlc.types.non_null(AspectRatios), graphql_name='aspectRatios')

    cameras = sgqlc.types.Field(sgqlc.types.non_null(Cameras), graphql_name='cameras')

    colorations = sgqlc.types.Field(sgqlc.types.non_null(Colorations), graphql_name='colorations')

    film_lengths = sgqlc.types.Field(sgqlc.types.non_null(FilmLengths), graphql_name='filmLengths')

    laboratories = sgqlc.types.Field(sgqlc.types.non_null(Laboratories), graphql_name='laboratories')

    negative_formats = sgqlc.types.Field(sgqlc.types.non_null(NegativeFormats), graphql_name='negativeFormats')

    printed_formats = sgqlc.types.Field(sgqlc.types.non_null(PrintedFormats), graphql_name='printedFormats')

    processes = sgqlc.types.Field(sgqlc.types.non_null(Processes), graphql_name='processes')

    sound_mixes = sgqlc.types.Field(sgqlc.types.non_null(SoundMixes), graphql_name='soundMixes')



class Test(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('error', 'experimental', 'result', 'test_items')
    error = sgqlc.types.Field(String, graphql_name='error')

    experimental = sgqlc.types.Field(String, graphql_name='experimental')

    result = sgqlc.types.Field(String, graphql_name='result')

    test_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TestItem')), graphql_name='testItems', args=sgqlc.types.ArgDict((
        ('cachebuster', sgqlc.types.Arg(String, graphql_name='cachebuster', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `cachebuster` (`String`)None
    * `limit` (`Int!`)None
    '''



class TestAuth(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cacheable_result', 'cacheable_result_with_no_cache_customer_id', 'cacheable_result_with_no_cache_user_id', 'client_ip', 'detected_country', 'has_authentication_headers', 'has_transitive_authentication_headers', 'non_cacheable_result', 'result')
    cacheable_result = sgqlc.types.Field(String, graphql_name='cacheableResult')

    cacheable_result_with_no_cache_customer_id = sgqlc.types.Field(String, graphql_name='cacheableResultWithNoCacheCustomerId')

    cacheable_result_with_no_cache_user_id = sgqlc.types.Field(String, graphql_name='cacheableResultWithNoCacheUserId')

    client_ip = sgqlc.types.Field(String, graphql_name='clientIp')

    detected_country = sgqlc.types.Field(String, graphql_name='detectedCountry')

    has_authentication_headers = sgqlc.types.Field(Boolean, graphql_name='hasAuthenticationHeaders')

    has_transitive_authentication_headers = sgqlc.types.Field(Boolean, graphql_name='hasTransitiveAuthenticationHeaders')

    non_cacheable_result = sgqlc.types.Field(String, graphql_name='nonCacheableResult')

    result = sgqlc.types.Field(String, graphql_name='result')



class TestAuthTimer(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('auth_timer',)
    auth_timer = sgqlc.types.Field(String, graphql_name='authTimer')



class TestEntitlement(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('entitlement', 'result')
    entitlement = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entitlement')

    result = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='result')



class TestItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class ThirdPartyTrackers(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('impression_trackers', 'title_poster_click_trackers', 'video_complete_trackers', 'video_first_quartile_trackers', 'video_midpoint_trackers', 'video_start_trackers', 'video_third_quartile_trackers')
    impression_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='impressionTrackers')

    title_poster_click_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='titlePosterClickTrackers')

    video_complete_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='videoCompleteTrackers')

    video_first_quartile_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='videoFirstQuartileTrackers')

    video_midpoint_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='videoMidpointTrackers')

    video_start_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='videoStartTrackers')

    video_third_quartile_trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(URL))), graphql_name='videoThirdQuartileTrackers')



class Thumbnail(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('height', 'url', 'width')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')



class TitleChartMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('chart_description', 'chart_name')
    chart_description = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='chartDescription')

    chart_name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='chartName')



class TitleChartRankingsNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('chart_rating', 'chart_vote_count', 'item')
    chart_rating = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='chartRating')

    chart_vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='chartVoteCount')

    item = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='item')



class TitleCinemaShowtimesByScreeningType(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('cinema', 'distance_to_cinema', 'id', 'showtimes_by_screening_type', 'title')
    cinema = sgqlc.types.Field(sgqlc.types.non_null(Cinema), graphql_name='cinema')

    distance_to_cinema = sgqlc.types.Field('DistanceToCinema', graphql_name='distanceToCinema')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    showtimes_by_screening_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ShowtimesByScreeningType))), graphql_name='showtimesByScreeningType')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class TitleConnection(sgqlc.types.relay.Connection):
    __schema__ = model
    __field_names__ = ('associated_title', 'category', 'description')
    associated_title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='associatedTitle')

    category = sgqlc.types.Field(sgqlc.types.non_null('TitleConnectionCategory'), graphql_name='category')

    description = sgqlc.types.Field(Markdown, graphql_name='description')



class TitleCoreCatalog(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('keywords',)
    keywords = sgqlc.types.Field(sgqlc.types.list_of(Experimental_KeywordItem), graphql_name='keywords')



class TitleCreditCategoryWithCredits(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'credits')
    category = sgqlc.types.Field(sgqlc.types.non_null('CreditCategory'), graphql_name='category')

    credits = sgqlc.types.Field('CreditConnection', graphql_name='credits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class TitleGenre(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('genre', 'relevance_ranking', 'sub_genres')
    genre = sgqlc.types.Field(sgqlc.types.non_null('GenreItem'), graphql_name='genre')

    relevance_ranking = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='relevanceRanking')

    sub_genres = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TitleKeyword')), graphql_name='subGenres')



class TitleGenreRecommendation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('explanation', 'label', 'ref_tag', 'titles')
    explanation = sgqlc.types.Field(sgqlc.types.non_null(LocalizedMarkdown), graphql_name='explanation')

    label = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='label')

    ref_tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTag')

    titles = sgqlc.types.Field('TitleGenreRecommendationConnection', graphql_name='titles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int!`)None
    '''



class TitleGenres(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('genres',)
    genres = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TitleGenre))), graphql_name='genres', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort', sgqlc.types.Arg(GenreSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    * `sort` (`GenreSort`)None
    '''



class TitleKeyword(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('interest_score', 'item_category', 'keyword', 'legacy_id')
    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    item_category = sgqlc.types.Field('TitleKeywordItemCategory', graphql_name='itemCategory')

    keyword = sgqlc.types.Field(sgqlc.types.non_null(Keyword), graphql_name='keyword')

    legacy_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='legacyId')



class TitleKeywordItemCategoryWithKeywords(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('item_category', 'keywords')
    item_category = sgqlc.types.Field(sgqlc.types.non_null('TitleKeywordItemCategory'), graphql_name='itemCategory')

    keywords = sgqlc.types.Field(sgqlc.types.non_null('TitleKeywordConnection'), graphql_name='keywords', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''



class TitleMetadata(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('external_link_categories', 'goof_categories', 'title_connection_categories', 'title_genres', 'title_type_categories', 'title_types')
    external_link_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ExternalLinkCategory'))), graphql_name='externalLinkCategories')

    goof_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GoofCategory'))), graphql_name='goofCategories')

    title_connection_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TitleConnectionCategory'))), graphql_name='titleConnectionCategories')

    title_genres = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GenreItem'))), graphql_name='titleGenres')

    title_type_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TitleTypeCategoryWithTitleTypes'))), graphql_name='titleTypeCategories')

    title_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TitleType'))), graphql_name='titleTypes', args=sgqlc.types.ArgDict((
        ('category', sgqlc.types.Arg(TitleTypeCategoryValue, graphql_name='category', default=None)),
))
    )
    '''Arguments:

    * `category` (`TitleTypeCategoryValue`)None
    '''



class TitleQuoteCharacter(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('character', 'name')
    character = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='character')

    name = sgqlc.types.Field('Name', graphql_name='name')



class TitleQuoteLine(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('characters', 'stage_direction', 'text')
    characters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleQuoteCharacter)), graphql_name='characters')

    stage_direction = sgqlc.types.Field(String, graphql_name='stageDirection')

    text = sgqlc.types.Field(String, graphql_name='text')



class TitleRecommendation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('explanations', 'ref_tag', 'title')
    explanations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RecommendationExplanation))), graphql_name='explanations')

    ref_tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTag')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class TitleText(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('country', 'is_original_title', 'language', 'text')
    country = sgqlc.types.Field('DisplayableCountry', graphql_name='country')

    is_original_title = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOriginalTitle')

    language = sgqlc.types.Field('DisplayableLanguage', graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class TitleTypeCategorySummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title_type_category', 'total')
    title_type_category = sgqlc.types.Field(sgqlc.types.non_null('TitleTypeCategory'), graphql_name='titleTypeCategory')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleTypeCategoryWithTitleTypes(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'title_types')
    category = sgqlc.types.Field(sgqlc.types.non_null('TitleTypeCategory'), graphql_name='category')

    title_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TitleType'))), graphql_name='titleTypes')



class TitleTypeSummary(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title_type', 'total')
    title_type = sgqlc.types.Field(sgqlc.types.non_null('TitleType'), graphql_name='titleType')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleWatchlistRecommendation(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('explanation', 'title')
    explanation = sgqlc.types.Field(sgqlc.types.non_null(LocalizedMarkdown), graphql_name='explanation')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class TopGrossingReleasesNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('gross', 'release')
    gross = sgqlc.types.Field(sgqlc.types.non_null(BoxOfficeGross), graphql_name='gross')

    release = sgqlc.types.Field(sgqlc.types.non_null(BoxOfficeRelease), graphql_name='release')



class TopRanking(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'rank', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')

    text = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='text')



class TotalCredits(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('CreditRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TrendingCollectionOption(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('country', 'data_window', 'traffic_source')
    country = sgqlc.types.Field(sgqlc.types.non_null('DisplayableCountry'), graphql_name='country')

    data_window = sgqlc.types.Field(sgqlc.types.non_null(TrendingDataWindow), graphql_name='dataWindow')

    traffic_source = sgqlc.types.Field(sgqlc.types.non_null(TrendingTrafficSource), graphql_name='trafficSource')



class TrendingNameCollection(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'option')
    items = sgqlc.types.Field(sgqlc.types.non_null('TrendingNameConnection'), graphql_name='items', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    option = sgqlc.types.Field(sgqlc.types.non_null(TrendingCollectionOption), graphql_name='option')



class TrendingNameCollectionOptions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('options', 'selected_item')
    options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TrendingCollectionOption))), graphql_name='options')

    selected_item = sgqlc.types.Field(sgqlc.types.non_null(TrendingNameCollection), graphql_name='selectedItem')



class TrendingNameNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('item', 'rank', 'weight_rank')
    item = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='item')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')

    weight_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightRank')



class TrendingTitleCollection(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('items', 'option')
    items = sgqlc.types.Field(sgqlc.types.non_null('TrendingTitleConnection'), graphql_name='items', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    option = sgqlc.types.Field(sgqlc.types.non_null(TrendingCollectionOption), graphql_name='option')



class TrendingTitleCollectionOptions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('options', 'selected_item')
    options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TrendingCollectionOption))), graphql_name='options')

    selected_item = sgqlc.types.Field(sgqlc.types.non_null(TrendingTitleCollection), graphql_name='selectedItem')



class TrendingTitleNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('item', 'rank', 'weight_rank')
    item = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='item')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')

    weight_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightRank')



class TrendingVideoNode(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('item', 'rank', 'weight_rank')
    item = sgqlc.types.Field(sgqlc.types.non_null('Video'), graphql_name='item')

    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')

    weight_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weightRank')



class TriviaCategoryWithTrivia(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('category', 'restriction', 'trivia')
    category = sgqlc.types.Field('TriviaCategory', graphql_name='category')

    restriction = sgqlc.types.Field('TriviaRestriction', graphql_name='restriction')

    trivia = sgqlc.types.Field('TriviaConnection', graphql_name='trivia', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TriviaCategoryWithTriviaFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `filter` (`TriviaCategoryWithTriviaFilter`)None
    * `first` (`Int`)None
    '''



class User(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('creation_date', 'display_name', 'feedback_given', 'full_name', 'interests', 'linked_auth_providers', 'preferred_language', 'preferred_streaming_providers', 'pro_status', 'profile', 'ratings_privacy', 'staff_status')
    creation_date = sgqlc.types.Field(DateTime, graphql_name='creationDate')

    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')

    feedback_given = sgqlc.types.Field(sgqlc.types.non_null(FeedbackGiven), graphql_name='feedbackGiven', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FeedbackGivenInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`FeedbackGivenInput!`)None
    '''

    full_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullName')

    interests = sgqlc.types.Field(sgqlc.types.non_null('UserInterestsConnection'), graphql_name='interests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(UserInterestsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`UserInterestsFilter`)None
    * `first` (`Int!`)None
    '''

    linked_auth_providers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LinkedAuthProvider))), graphql_name='linkedAuthProviders')

    preferred_language = sgqlc.types.Field(String, graphql_name='preferredLanguage')

    preferred_streaming_providers = sgqlc.types.Field(sgqlc.types.non_null('UserPreferredStreamingProvidersOutput'), graphql_name='preferredStreamingProviders', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(UserPreferredStreamingProvidersInput, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`UserPreferredStreamingProvidersInput`)None
    * `first` (`Int!`)None
    '''

    pro_status = sgqlc.types.Field(ProStatus, graphql_name='proStatus')

    profile = sgqlc.types.Field(sgqlc.types.non_null('UserProfile'), graphql_name='profile')

    ratings_privacy = sgqlc.types.Field('RatingsPrivacy', graphql_name='ratingsPrivacy')

    staff_status = sgqlc.types.Field(StaffStatus, graphql_name='staffStatus')



class UserConsentOutput(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('consent', 'consent_operation', 'consent_type')
    consent = sgqlc.types.Field(Consent, graphql_name='consent')

    consent_operation = sgqlc.types.Field(ConsentOperation, graphql_name='consentOperation')

    consent_type = sgqlc.types.Field(sgqlc.types.non_null(ConsentType), graphql_name='consentType')



class UserPreferredStreamingProvidersOutput(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('streaming_providers', 'total')
    streaming_providers = sgqlc.types.Field(sgqlc.types.non_null('WatchProviderConnection'), graphql_name='streamingProviders')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class UserProfile(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('creation_date', 'nick_name', 'user_id')
    creation_date = sgqlc.types.Field(DateTime, graphql_name='creationDate')

    nick_name = sgqlc.types.Field(String, graphql_name='nickName')

    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')



class UserReaction(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('entity_id', 'last_updated', 'reaction')
    entity_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='entityId')

    last_updated = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastUpdated')

    reaction = sgqlc.types.Field(sgqlc.types.non_null('Reaction'), graphql_name='reaction')



class Video(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('app_ad_url', 'content_type', 'created_date', 'description', 'id', 'is_mature', 'name', 'personalized_suggested_videos', 'playback_urls', 'preview_urls', 'primary_title', 'provider_type', 'reactions_summary', 'recommended_timed_text_track', 'related_names', 'related_titles', 'related_videos', 'runtime', 'thumbnail', 'timed_text_tracks', 'user_reactions', 'video_dimensions', 'web_ad_url')
    app_ad_url = sgqlc.types.Field(URL, graphql_name='appAdURL', args=sgqlc.types.ArgDict((
        ('ad_parameters', sgqlc.types.Arg(sgqlc.types.non_null(AdParametersApp), graphql_name='adParameters', default=None)),
))
    )
    '''Arguments:

    * `ad_parameters` (`AdParametersApp!`)None
    '''

    content_type = sgqlc.types.Field('VideoContentType', graphql_name='contentType')

    created_date = sgqlc.types.Field(DateTime, graphql_name='createdDate')

    description = sgqlc.types.Field(LocalizedString, graphql_name='description')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_mature = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMature')

    name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='name')

    personalized_suggested_videos = sgqlc.types.Field('PersonalizedSuggestedVideosConnection', graphql_name='personalizedSuggestedVideos', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    playback_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PlaybackURL))), graphql_name='playbackURLs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(VideoContentFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`VideoContentFilter`)None
    '''

    preview_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PlaybackURL))), graphql_name='previewURLs')

    primary_title = sgqlc.types.Field('Title', graphql_name='primaryTitle')

    provider_type = sgqlc.types.Field(sgqlc.types.non_null('VideoProviderType'), graphql_name='providerType')

    reactions_summary = sgqlc.types.Field(ReactionsSummary, graphql_name='reactionsSummary')

    recommended_timed_text_track = sgqlc.types.Field('VideoTimedTextTrack', graphql_name='recommendedTimedTextTrack', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RecommendedVideoTimedTextTrackFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`RecommendedVideoTimedTextTrackFilter`)None
    '''

    related_names = sgqlc.types.Field('VideoNameRelationConnection', graphql_name='relatedNames', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    related_titles = sgqlc.types.Field('VideoTitleRelationConnection', graphql_name='relatedTitles', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    related_videos = sgqlc.types.Field('VideoConnection', graphql_name='relatedVideos', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    runtime = sgqlc.types.Field('VideoRuntime', graphql_name='runtime')

    thumbnail = sgqlc.types.Field(sgqlc.types.non_null(Thumbnail), graphql_name='thumbnail')

    timed_text_tracks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('VideoTimedTextTrack')), graphql_name='timedTextTracks', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(VideoTimedTextTracksFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`VideoTimedTextTracksFilter`)None
    '''

    user_reactions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserReaction)), graphql_name='userReactions')

    video_dimensions = sgqlc.types.Field('VideoDimensions', graphql_name='videoDimensions')

    web_ad_url = sgqlc.types.Field(URL, graphql_name='webAdURL', args=sgqlc.types.ArgDict((
        ('ad_parameters', sgqlc.types.Arg(sgqlc.types.non_null(AdParametersWeb), graphql_name='adParameters', default=None)),
))
    )
    '''Arguments:

    * `ad_parameters` (`AdParametersWeb!`)None
    '''



class VideoContentType(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('display_name', 'id')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='displayName')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class VideoDimensions(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('appearance', 'aspect_ratio', 'height', 'width')
    appearance = sgqlc.types.Field(sgqlc.types.non_null(VideoAppearance), graphql_name='appearance')

    aspect_ratio = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='aspectRatio')

    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')

    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')



class VideoFacets(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('names', 'titles', 'types')
    names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('VideoNameFacet')), graphql_name='names')

    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('VideoTitleFacet')), graphql_name='titles')

    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('VideoTypeFacet')), graphql_name='types')



class VideoMedia(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id', 'name', 'primary_image', 'runtime')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='name')

    primary_image = sgqlc.types.Field('MediaServiceImage', graphql_name='primaryImage')

    runtime = sgqlc.types.Field('VideoRuntime', graphql_name='runtime')



class VideoNameFacet(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('name', 'total')
    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class VideoProviderType(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')



class VideoRecommendationsAdItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('ad_type', 'transition_delay')
    ad_type = sgqlc.types.Field(sgqlc.types.non_null(VideoRecommendationsAdType), graphql_name='adType')

    transition_delay = sgqlc.types.Field(Float, graphql_name='transitionDelay')



class VideoRecommendationsVideoItem(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('video',)
    video = sgqlc.types.Field(Video, graphql_name='video')



class VideoRuntime(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('unit', 'value')
    unit = sgqlc.types.Field(sgqlc.types.non_null(TimeUnit), graphql_name='unit')

    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')



class VideoTimedTextTrack(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('display_name', 'language', 'ref_tag_fragment', 'type', 'url')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='displayName')

    language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='language')

    ref_tag_fragment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTagFragment')

    type = sgqlc.types.Field(sgqlc.types.non_null(VideoTimedTextTrackType), graphql_name='type')

    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')



class VideoTitleFacet(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('title', 'total')
    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class VideoTypeFacet(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('total', 'type')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')

    type = sgqlc.types.Field(sgqlc.types.non_null(VideoContentType), graphql_name='type')



class VideoTypeWithVideos(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('video_type', 'videos')
    video_type = sgqlc.types.Field(sgqlc.types.non_null(VideoContentType), graphql_name='videoType')

    videos = sgqlc.types.Field('VideoTypesConnection', graphql_name='videos', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''



class WatchOption(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('description', 'link', 'promoted', 'provider', 'provider_name', 'provider_ref_tag_fragment', 'short_description', 'short_title', 'title')
    description = sgqlc.types.Field(LocalizedString, graphql_name='description')

    link = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='link', args=sgqlc.types.ArgDict((
        ('platform', sgqlc.types.Arg(sgqlc.types.non_null(PlatformLinkFormatId), graphql_name='platform', default=None)),
))
    )
    '''Arguments:

    * `platform` (`PlatformLinkFormatId!`)None
    '''

    promoted = sgqlc.types.Field(Boolean, graphql_name='promoted')

    provider = sgqlc.types.Field(sgqlc.types.non_null('WatchProvider'), graphql_name='provider')

    provider_name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='providerName')

    provider_ref_tag_fragment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='providerRefTagFragment')

    short_description = sgqlc.types.Field(LocalizedString, graphql_name='shortDescription')

    short_title = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='shortTitle')

    title = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='title')



class WatchProvider(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('description', 'id', 'is_popular', 'is_supported', 'logos', 'name', 'ref_tag_fragment', 'watch_option_category_type')
    description = sgqlc.types.Field(LocalizedString, graphql_name='description')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    is_popular = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPopular')

    is_supported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSupported', args=sgqlc.types.ArgDict((
        ('platform', sgqlc.types.Arg(sgqlc.types.non_null(PlatformId), graphql_name='platform', default=None)),
))
    )
    '''Arguments:

    * `platform` (`PlatformId!`)None
    '''

    logos = sgqlc.types.Field('WatchProviderLogos', graphql_name='logos')

    name = sgqlc.types.Field(sgqlc.types.non_null(LocalizedString), graphql_name='name')

    ref_tag_fragment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTagFragment')

    watch_option_category_type = sgqlc.types.Field(WatchOptionCategoryType, graphql_name='watchOptionCategoryType')



class WatchProviderLogos(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('icon', 'slate')
    icon = sgqlc.types.Field('MediaServiceImage', graphql_name='icon')

    slate = sgqlc.types.Field('MediaServiceImage', graphql_name='slate')



class WatchlistStatistics(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('displayable_count', 'total_count')
    displayable_count = sgqlc.types.Field('LocalizedDisplayableCount', graphql_name='displayableCount')

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')



class WebviewVideoPlayer(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('audio_language', 'burned_in_captions_language', 'description', 'webview_url')
    audio_language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='audioLanguage')

    burned_in_captions_language = sgqlc.types.Field(Language, graphql_name='burnedInCaptionsLanguage')

    description = sgqlc.types.Field(LocalizedString, graphql_name='description')

    webview_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='webviewUrl')



class WorkAuthorizationCountries(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('total', 'work_authorizations')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')

    work_authorizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkAuthorizationInCountry'))), graphql_name='workAuthorizations')



class WorkAuthorizationInCountry(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('country', 'is_authorized')
    country = sgqlc.types.Field(sgqlc.types.non_null('LocalizedDisplayableCountry'), graphql_name='country')

    is_authorized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAuthorized')



class YearRange(sgqlc.types.Type):
    __schema__ = model
    __field_names__ = ('end_year', 'year')
    end_year = sgqlc.types.Field(Int, graphql_name='endYear')

    year = sgqlc.types.Field(Int, graphql_name='year')



class AdvancedNameSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facet', 'total')
    facet = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchFacet')), graphql_name='facet', args=sgqlc.types.ArgDict((
        ('facet_field', sgqlc.types.Arg(sgqlc.types.non_null(NameFacetField), graphql_name='facetField', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `facet_field` (`NameFacetField!`)None
    * `limit` (`Int`)None
    '''

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AdvancedNameSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(AdvancedNameSearchResult), graphql_name='node')



class AdvancedTitleSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facet', 'total')
    facet = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchFacet')), graphql_name='facet', args=sgqlc.types.ArgDict((
        ('facet_field', sgqlc.types.Arg(sgqlc.types.non_null(TitleFacetField), graphql_name='facetField', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `facet_field` (`TitleFacetField!`)None
    * `limit` (`Int`)None
    '''

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AdvancedTitleSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(AdvancedTitleSearchResult), graphql_name='node')



class AgeDetails(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')



class Aka(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'country', 'language', 'text')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    country = sgqlc.types.Field('DisplayableCountry', graphql_name='country')

    language = sgqlc.types.Field('DisplayableLanguage', graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class AkaConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AkaEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Aka), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class AlternateVersion(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class AlternateVersionConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AlternateVersionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(AlternateVersion), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class AmazonMusicProductArtistName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class AmazonMusicProductFormat(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class AmazonMusicProductTitle(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class AnswerOption(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class AspectRatio(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('aspect_ratio', 'attributes')
    aspect_ratio = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aspectRatio')

    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')



class AuthProviderDeprecationUrlLabel(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class AwardCompany(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('company', 'note')
    company = sgqlc.types.Field(sgqlc.types.non_null('Company'), graphql_name='company')

    note = sgqlc.types.Field(Markdown, graphql_name='note')



class AwardDetails(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ('award_nomination_categories', 'event_edition')
    award_nomination_categories = sgqlc.types.Field('AwardNominationsWithCategoryConnection', graphql_name='awardNominationCategories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    event_edition = sgqlc.types.Field(sgqlc.types.non_null(EventEdition), graphql_name='eventEdition')



class AwardDetailsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AwardDetailsEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(AwardDetails), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class AwardName(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('name', 'note')
    name = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='name')

    note = sgqlc.types.Field(Markdown, graphql_name='note')



class AwardNominationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AwardNominationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(AwardNomination), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class AwardNominationsWithCategoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class AwardNominationsWithCategoryEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(AwardNominationsWithCategory), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class AwardTitle(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('note', 'title')
    note = sgqlc.types.Field(Markdown, graphql_name='note')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class AwardsEvent(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ('editions', 'location', 'trivia', 'urls')
    editions = sgqlc.types.Field('EventEditionConnection', graphql_name='editions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    location = sgqlc.types.Field('DisplayableLocation', graphql_name='location')

    trivia = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Markdown)), graphql_name='trivia')

    urls = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EventUrl)), graphql_name='urls')



class BackfillMessage(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class Banner(sgqlc.types.Type, ImageObject):
    __schema__ = model
    __field_names__ = ('attribution_url', 'image_url')
    attribution_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='attributionUrl')

    image_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageUrl')



class BirthName(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class BlogLink(sgqlc.types.Type, Link):
    __schema__ = model
    __field_names__ = ()


class BoxOfficeAreaType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('code',)
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')



class CallToActionImage(sgqlc.types.Type, ImageObject):
    __schema__ = model
    __field_names__ = ('caption',)
    caption = sgqlc.types.Field(LocalizedMarkdown, graphql_name='caption')



class Camera(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'camera')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    camera = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='camera')



class CertificatesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CertificatesEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Certificate), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ChartNameEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('current_rank', 'node', 'rank_change')
    current_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentRank')

    node = sgqlc.types.Field(sgqlc.types.non_null('Name'), graphql_name='node')

    rank_change = sgqlc.types.Field(RankChange, graphql_name='rankChange')



class ChartNameSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facet', 'total')
    facet = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchFacet')), graphql_name='facet', args=sgqlc.types.ArgDict((
        ('facet_field', sgqlc.types.Arg(sgqlc.types.non_null(NameFacetField), graphql_name='facetField', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `facet_field` (`NameFacetField!`)None
    * `limit` (`Int`)None
    '''

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ChartTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('current_rank', 'node', 'rank_change')
    current_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentRank')

    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    rank_change = sgqlc.types.Field(RankChange, graphql_name='rankChange')



class ChartTitleSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facet', 'my_rated_count', 'my_rated_percentage', 'total')
    facet = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchFacet')), graphql_name='facet', args=sgqlc.types.ArgDict((
        ('facet_field', sgqlc.types.Arg(sgqlc.types.non_null(TitleFacetField), graphql_name='facetField', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `facet_field` (`TitleFacetField!`)None
    * `limit` (`Int`)None
    '''

    my_rated_count = sgqlc.types.Field(Int, graphql_name='myRatedCount')

    my_rated_percentage = sgqlc.types.Field(LocalizedString, graphql_name='myRatedPercentage')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CinemaLocation(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CinemaName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class Coloration(sgqlc.types.Type, DisplayableConcept, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'concept_id')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    concept_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='conceptId')



class Company(sgqlc.types.Type, PrimaryConst):
    __schema__ = model
    __field_names__ = ('acronyms', 'affiliations', 'bio', 'company_text', 'company_types', 'country', 'images', 'key_staff', 'known_for_clients', 'known_for_titles', 'managed_data', 'meter_ranking', 'meter_ranking_history', 'primary_image')
    acronyms = sgqlc.types.Field('CompanyAcronymConnection', graphql_name='acronyms', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    affiliations = sgqlc.types.Field('CompanyAffiliationConnection', graphql_name='affiliations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    bio = sgqlc.types.Field('CompanyBio', graphql_name='bio')

    company_text = sgqlc.types.Field(CompanyText, graphql_name='companyText')

    company_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompanyType')), graphql_name='companyTypes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    country = sgqlc.types.Field('LocalizedDisplayableCountry', graphql_name='country')

    images = sgqlc.types.Field('ImageConnection', graphql_name='images', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('bust', sgqlc.types.Arg(String, graphql_name='bust', default=None)),
        ('filter', sgqlc.types.Arg(CompanyImagesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `bust` (`String`)None
    * `filter` (`CompanyImagesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    key_staff = sgqlc.types.Field('CompanyKeyStaffConnection', graphql_name='keyStaff', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    known_for_clients = sgqlc.types.Field('CompanyKnownForClientConnection', graphql_name='knownForClients', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    known_for_titles = sgqlc.types.Field('CompanyKnownForTitleConnection', graphql_name='knownForTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''

    managed_data = sgqlc.types.Field(ManagedCompanyData, graphql_name='managedData')

    meter_ranking = sgqlc.types.Field('CompanyMeterRanking', graphql_name='meterRanking')

    meter_ranking_history = sgqlc.types.Field('CompanyMeterRankingHistory', graphql_name='meterRankingHistory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CompanyMeterRankingHistoryInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CompanyMeterRankingHistoryInput`)None
    '''

    primary_image = sgqlc.types.Field('Image', graphql_name='primaryImage')



class CompanyAcronym(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyAcronymConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyAcronymEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CompanyAcronym), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyAffiliation(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')



class CompanyAffiliationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyAffiliationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CompanyAffiliation), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyBio(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('id', 'language', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class CompanyCredit(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'category', 'company', 'countries', 'distribution_formats', 'title', 'years_involved')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    category = sgqlc.types.Field(sgqlc.types.non_null('CompanyCreditCategory'), graphql_name='category')

    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')

    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DisplayableCountry')), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    distribution_formats = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DistributionFormat')), graphql_name='distributionFormats')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')

    years_involved = sgqlc.types.Field(YearRange, graphql_name='yearsInvolved')



class CompanyCreditCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyCreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('CompanyCreditRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyCreditEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CompanyCredit), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyCreditRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class CompanyEmployeeOccupation(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyEmployeeTitle(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyJob(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyKeyStaffConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('record_pool_size', 'total')
    record_pool_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='recordPoolSize')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyKeyStaffEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CompanyKeyStaff), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyKeyStaffVersionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForKeyStaffVersion'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyKnownForClientConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('record_pool_size', 'total')
    record_pool_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='recordPoolSize')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyKnownForClientEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForClient), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyKnownForClientVersionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForClientVersion'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyKnownForCreditCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyKnownForTitleConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('record_pool_size', 'total')
    record_pool_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='recordPoolSize')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyKnownForTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForTitle), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyKnownForTitleVersionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('ManagedCompanyKnownForTitleVersion'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CompanyMeterRanking(sgqlc.types.Type, MeterRanking):
    __schema__ = model
    __field_names__ = ()


class CompanyMeterRankingHistory(sgqlc.types.Type, MeterRankingHistory):
    __schema__ = model
    __field_names__ = ()


class CompanyRepresentationCategories(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CompanyRepresentationCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CompanyType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ConnectionDescription(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ContributorLeaderboardConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class ContributorLeaderboardEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(ContributorLeaderboard), graphql_name='node')



class ContributorLeaderboardRankConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class ContributorLeaderboardRankEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(ContributorLeaderboardRank), graphql_name='node')



class ContributorRankEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(ContributorRank), graphql_name='node')



class ContributorRankingsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class CountryOfOrigin(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CrazyCredit(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('id', 'interest_score', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class CrazyCreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CrazyCreditEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(CrazyCredit), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CreditCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('completeness_status', 'order_by', 'restriction', 'total')
    completeness_status = sgqlc.types.Field('CreditsCompletenessStatus', graphql_name='completenessStatus', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CreditsCompletenessStatusFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`CreditsCompletenessStatusFilter`)None
    '''

    order_by = sgqlc.types.Field('CreditsOrderedBy', graphql_name='orderBy')

    restriction = sgqlc.types.Field('CreditRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class CreditEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Credit), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class CreditRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class CreditsCompletenessStatus(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class CreditsOrderedBy(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DemographicDataComponent(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DemographicDataType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(DemographicDataTypeValue), graphql_name='value')



class DemographicDataValue(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('components',)
    components = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DemographicDataComponent))), graphql_name='components')



class DisplayableAwardedEntity(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableBirthNameProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableCountry(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DisplayableDate(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('date', 'date_components')
    date = sgqlc.types.Field(Date, graphql_name='date')

    date_components = sgqlc.types.Field(DateComponents, graphql_name='dateComponents')



class DisplayableDateProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null('DisplayableLanguage'), graphql_name='language')



class DisplayableExternalLinkProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableLanguage(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DisplayableLocation(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(String, graphql_name='text')



class DisplayableLocationProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableNameAgeDetailsProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableNameAkaProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableNameDeathCause(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(String, graphql_name='text')



class DisplayableNameDeathCauseProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableNameHeightProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableNameOtherWorkProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ()


class DisplayableNameSpouseProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableNickNameProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableProfession(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DisplayableProfessionCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DisplayableProfessionDescription(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DisplayableRelationNameProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableSalaryProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayablePropertyKey):
    __schema__ = model
    __field_names__ = ()


class DisplayableSeasonConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class DisplayableSeasonEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('LocalizedDisplayableSeason'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class DisplayableSongTitle(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class DisplayableSpouseTimeRange(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('from_date', 'to_date')
    from_date = sgqlc.types.Field(DisplayableDate, graphql_name='fromDate')

    to_date = sgqlc.types.Field(DisplayableDate, graphql_name='toDate')



class DisplayableSpouseTimeRangeProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableTechnicalSpecificationLocalizedProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableTechnicalSpecificationProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ()


class DisplayableTitleAkaProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayablePropertyKey, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(DisplayableLanguage, graphql_name='language')



class DisplayableTitleCompanyCreditProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ()


class DisplayableTitleCountryOfOriginProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableTitleFilmingLocationProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(DisplayableLanguage, graphql_name='language')



class DisplayableTitleGenreProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableTitleReleaseDateProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayablePropertyKey, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ()


class DisplayableTitleRuntimeProperty(sgqlc.types.Type, DisplayableProperty, HasDisplayableQualifier):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableTitleSpokenLanguageProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class DisplayableTitleTaglineProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableTitleTypeProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class DisplayableYearConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class DisplayableYearEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('LocalizedDisplayableEpisodeYear'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class DistanceToCinema(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('distance_in_meters',)
    distance_in_meters = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distanceInMeters')



class DistributionFormat(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class EmployeeBranchName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class EpisodeConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class EpisodeEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class EpisodeNumberDisplayableProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class EventConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class EventEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(AwardsEvent), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class EventEditionConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class EventEditionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(EventEdition), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class EventUrlCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('category_id',)
    category_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='categoryId')



class ExperimentalCreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('completeness_status', 'order_by', 'restriction', 'total')
    completeness_status = sgqlc.types.Field(CreditsCompletenessStatus, graphql_name='completenessStatus')

    order_by = sgqlc.types.Field(CreditsOrderedBy, graphql_name='orderBy')

    restriction = sgqlc.types.Field(CreditRestriction, graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ExperimentalCreditEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ExperimentalCredit), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ExperimentalNameCreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('order_by', 'restriction', 'total')
    order_by = sgqlc.types.Field(CreditsOrderedBy, graphql_name='orderBy')

    restriction = sgqlc.types.Field(CreditRestriction, graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ExperimentalNominationAward(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ('award_nomination_categories',)
    award_nomination_categories = sgqlc.types.Field('ExperimentalNominationsWithCategoryConnection', graphql_name='awardNominationCategories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''



class ExperimentalNominationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ExperimentalNominationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ExperimentalNomination), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ExperimentalNominationsWithCategoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ExperimentalNominationsWithCategoryEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ExperimentalNominationsWithCategory), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Experimental_NotificationPreferenceType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class Experimental_UIWorkflowCheckboxFormElement(sgqlc.types.Type, Experimental_UIWorkflowFormElementWithFeedback, Experimental_UIWorkflowFormInputElement):
    __schema__ = model
    __field_names__ = ('boolean_value',)
    boolean_value = sgqlc.types.Field(Boolean, graphql_name='booleanValue')



class Experimental_UIWorkflowFeedbackFormElement(sgqlc.types.Type, Experimental_UIWorkflowFormElement, Experimental_UIWorkflowFormInputElement):
    __schema__ = model
    __field_names__ = ('boolean_value', 'feedback_type', 'messages')
    boolean_value = sgqlc.types.Field(Boolean, graphql_name='booleanValue')

    feedback_type = sgqlc.types.Field(sgqlc.types.non_null(Experimental_UIWorkflowFeedbackType), graphql_name='feedbackType')

    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LocalizedMarkdown))), graphql_name='messages')



class Experimental_UIWorkflowRadioGroupFormElement(sgqlc.types.Type, Experimental_UIWorkflowFormElementWithFeedback, Experimental_UIWorkflowFormInputElement):
    __schema__ = model
    __field_names__ = ('radio_constraints', 'radio_options', 'selected_radio_value')
    radio_constraints = sgqlc.types.Field(Experimental_RadioGroupFormConstraints, graphql_name='radioConstraints')

    radio_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Experimental_RadioOption)), graphql_name='radioOptions')

    selected_radio_value = sgqlc.types.Field(String, graphql_name='selectedRadioValue')



class Experimental_UIWorkflowTextAreaFormElement(sgqlc.types.Type, Experimental_UIWorkflowFormElementWithFeedback):
    __schema__ = model
    __field_names__ = ('text_constraints', 'text_value')
    text_constraints = sgqlc.types.Field(Experimental_TextFormElementConstraints, graphql_name='textConstraints')

    text_value = sgqlc.types.Field(String, graphql_name='textValue')



class Experimental_UIWorkflowTextFormElement(sgqlc.types.Type, Experimental_UIWorkflowFormElementWithFeedback, Experimental_UIWorkflowFormInputElement):
    __schema__ = model
    __field_names__ = ('text_constraints', 'text_value')
    text_constraints = sgqlc.types.Field(Experimental_TextFormElementConstraints, graphql_name='textConstraints')

    text_value = sgqlc.types.Field(String, graphql_name='textValue')



class ExportDetailConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ExportDetailEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(ExportDetail), graphql_name='node')



class ExportStatusName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ExternalLink(sgqlc.types.Type, HasDisplayableProperty, Link):
    __schema__ = model
    __field_names__ = ('external_link_category', 'external_link_languages', 'external_link_region', 'id', 'label_language')
    external_link_category = sgqlc.types.Field(sgqlc.types.non_null('ExternalLinkCategory'), graphql_name='externalLinkCategory')

    external_link_languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableLanguage)), graphql_name='externalLinkLanguages')

    external_link_region = sgqlc.types.Field(DisplayableCountry, graphql_name='externalLinkRegion')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    label_language = sgqlc.types.Field(DisplayableLanguage, graphql_name='labelLanguage')



class ExternalLinkCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ExternalLinkConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('ExternalLinkRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ExternalLinkEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ExternalLink), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ExternalLinkRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class FanPicksConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('ref_tag',)
    ref_tag = sgqlc.types.Field(RefTag, graphql_name='refTag')



class FanPicksEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class FaqConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class FaqEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Faq), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class FilmLength(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'countries', 'film_length', 'is_split_reel', 'num_reels')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableCountry)), graphql_name='countries')

    film_length = sgqlc.types.Field(Float, graphql_name='filmLength')

    is_split_reel = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSplitReel')

    num_reels = sgqlc.types.Field(Float, graphql_name='numReels')



class FilmingDatesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class FilmingDatesEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(FilmingDates), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class FilmingLocation(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('attributes', 'interest_score', 'location')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute)), graphql_name='attributes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    location = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='location')



class FilmingLocationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('FilmingLocationRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class FilmingLocationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(FilmingLocation), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class FilmingLocationRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class GenderIdentity(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class GenreItem(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('genre_id',)
    genre_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='genreId')



class Goof(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('category', 'id', 'interest_score', 'is_spoiler', 'text')
    category = sgqlc.types.Field(sgqlc.types.non_null('GoofCategory'), graphql_name='category')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    is_spoiler = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSpoiler')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class GoofCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class GoofConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class GoofEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Goof), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Image(sgqlc.types.Type, ImageObject):
    __schema__ = model
    __field_names__ = ('caption', 'copyright', 'correction_link', 'countries', 'created_by', 'created_on', 'id', 'languages', 'names', 'reporting_link', 'source', 'titles', 'type')
    caption = sgqlc.types.Field(Markdown, graphql_name='caption')

    copyright = sgqlc.types.Field(String, graphql_name='copyright')

    correction_link = sgqlc.types.Field(ContributionLink, graphql_name='correctionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
        ('related_id', sgqlc.types.Arg(ID, graphql_name='relatedId', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    * `related_id` (`ID`)None
    '''

    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableCountry)), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    created_by = sgqlc.types.Field(String, graphql_name='createdBy')

    created_on = sgqlc.types.Field(DisplayableDate, graphql_name='createdOn')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    languages = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableLanguage)), graphql_name='languages', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Name')), graphql_name='names', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    reporting_link = sgqlc.types.Field(ContributionLink, graphql_name='reportingLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
        ('related_id', sgqlc.types.Arg(ID, graphql_name='relatedId', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    * `related_id` (`ID`)None
    '''

    source = sgqlc.types.Field(Source, graphql_name='source')

    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Title')), graphql_name='titles', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    type = sgqlc.types.Field(String, graphql_name='type')



class ImageConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facets', 'is_pagination_dirty', 'restriction', 'total')
    facets = sgqlc.types.Field(ImageFacets, graphql_name='facets')

    is_pagination_dirty = sgqlc.types.Field(Boolean, graphql_name='isPaginationDirty')

    restriction = sgqlc.types.Field('ImageRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ImageEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Image), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ImageGalleryFacetConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ImageGalleryFacetEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position', 'total')
    node = sgqlc.types.Field(sgqlc.types.non_null(ImageGallery), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ImageRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class ImageType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('image_type_id',)
    image_type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imageTypeId')



class ImageTypesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field(ImageRestriction, graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class InterestCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('interests',)
    interests = sgqlc.types.Field('InterestConnection', graphql_name='interests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''



class InterestCategoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class InterestCategoryEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(InterestCategory), graphql_name='node')



class InterestConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class InterestEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Interest), graphql_name='node')



class InterestImportanceScore(sgqlc.types.Type, Score):
    __schema__ = model
    __field_names__ = ()


class InterestSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class InterestSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Interest), graphql_name='node')



class InterestText(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class KeywordText(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class KeywordTitleConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class KeywordTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Laboratory(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'credited_as', 'is_uncredited', 'laboratory')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    credited_as = sgqlc.types.Field(String, graphql_name='creditedAs')

    is_uncredited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUncredited')

    laboratory = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='laboratory')



class ListClassName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ListConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('is_pagination_dirty', 'jump_to_found', 'total')
    is_pagination_dirty = sgqlc.types.Field(Boolean, graphql_name='isPaginationDirty')

    jump_to_found = sgqlc.types.Field(Boolean, graphql_name='jumpToFound')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ListItemEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ListItemNode), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ListVisibilityName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class LocalizedDisplayableCount(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class LocalizedDisplayableCountry(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ('language',)
    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')



class LocalizedDisplayableEpisodeNumber(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('episode_number',)
    episode_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='episodeNumber')



class LocalizedDisplayableEpisodeYear(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('year',)
    year = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='year')



class LocalizedDisplayableSeason(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('season',)
    season = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='season')



class MainSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class MainSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(MainSearchNode), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ManagedCompanyKeyStaffCategory(sgqlc.types.Type, ManagedCompanyKnownForCategory):
    __schema__ = model
    __field_names__ = ('staff',)
    staff = sgqlc.types.Field(sgqlc.types.non_null(CompanyKeyStaffConnection), graphql_name='staff', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKeyStaffHistoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ManagedCompanyKnownForClientCategory(sgqlc.types.Type, ManagedCompanyKnownForCategory):
    __schema__ = model
    __field_names__ = ('clients',)
    clients = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForClientConnection), graphql_name='clients', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKnownForClientHistoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ManagedCompanyKnownForClientVersion(sgqlc.types.Type, ManagedCompanyKnownForCategoryVersion):
    __schema__ = model
    __field_names__ = ('clients',)
    clients = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForClientConnection), graphql_name='clients', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKnownForKeyStaffVersion(sgqlc.types.Type, ManagedCompanyKnownForCategoryVersion):
    __schema__ = model
    __field_names__ = ('staff',)
    staff = sgqlc.types.Field(sgqlc.types.non_null(CompanyKeyStaffConnection), graphql_name='staff', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKnownForTitleCategory(sgqlc.types.Type, ManagedCompanyKnownForCategory):
    __schema__ = model
    __field_names__ = ('titles',)
    titles = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForTitleConnection), graphql_name='titles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class ManagedCompanyKnownForTitleHistoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ManagedCompanyKnownForTitleVersion(sgqlc.types.Type, ManagedCompanyKnownForCategoryVersion):
    __schema__ = model
    __field_names__ = ('titles',)
    titles = sgqlc.types.Field(sgqlc.types.non_null(CompanyKnownForTitleConnection), graphql_name='titles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    '''



class MediaServiceImage(sgqlc.types.Type, ImageObject):
    __schema__ = model
    __field_names__ = ()


class MetacriticReviewConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class MetacriticReviewEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(MetacriticReview), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class MeterRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ()


class Name(sgqlc.types.Type, PrimaryConst):
    __schema__ = model
    __field_names__ = ('age', 'akas', 'alexa_top_questions', 'auto_selected_professions', 'award_nominations', 'bio', 'bios', 'birth_date', 'birth_location', 'birth_name', 'canonical_url', 'content_warnings', 'credit_categories', 'credit_summary', 'credits', 'death_cause', 'death_date', 'death_location', 'death_status', 'demographic_data', 'disambiguator', 'engagement_statistics', 'experimental_credit_categories', 'experimental_credits', 'experimental_resume', 'experimental_track_notification_preferences', 'external_link_categories', 'external_links', 'featured_external_link_categories', 'featured_polls', 'height', 'image_types', 'image_upload_link', 'images', 'is_claimed', 'known_for', 'managed_data', 'meta', 'meter_ranking', 'meter_ranking_history', 'more_like_this_names', 'name_text', 'news', 'nick_names', 'nominations', 'other_works', 'prestigious_award_summary', 'primary_image', 'primary_professions', 'primary_videos', 'professions', 'publicity_categories', 'publicity_listings', 'quotes', 'related_lists', 'relations', 'search_indexing', 'self_verified_data', 'shared_names', 'shared_titles', 'spouses', 'title_salaries', 'trademarks', 'trivia', 'user_selected_professions', 'vanity_url', 'video_types', 'videos')
    age = sgqlc.types.Field(AgeDetails, graphql_name='age', args=sgqlc.types.ArgDict((
        ('current_date', sgqlc.types.Arg(Date, graphql_name='currentDate', default=None)),
))
    )
    '''Arguments:

    * `current_date` (`Date`)None
    '''

    akas = sgqlc.types.Field('NameAkaConnection', graphql_name='akas', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    alexa_top_questions = sgqlc.types.Field(AlexaQuestionConnection, graphql_name='alexaTopQuestions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    auto_selected_professions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameProfession)), graphql_name='autoSelectedProfessions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    award_nominations = sgqlc.types.Field(AwardNominationConnection, graphql_name='awardNominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(AwardNominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(AwardNominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`AwardNominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`AwardNominationsSort`)None
    '''

    bio = sgqlc.types.Field('NameBio', graphql_name='bio')

    bios = sgqlc.types.Field('NameBiosConnection', graphql_name='bios', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NameBiosFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NameBiosFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    birth_date = sgqlc.types.Field(DisplayableDate, graphql_name='birthDate')

    birth_location = sgqlc.types.Field(DisplayableLocation, graphql_name='birthLocation')

    birth_name = sgqlc.types.Field(BirthName, graphql_name='birthName')

    canonical_url = sgqlc.types.Field(String, graphql_name='canonicalUrl')

    content_warnings = sgqlc.types.Field(ContentWarnings, graphql_name='contentWarnings')

    credit_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameCreditCategoryWithCredits)), graphql_name='creditCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NameCreditCategoryFilter, graphql_name='filter', default=None)),
        ('sort', sgqlc.types.Arg(NameCreditSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `filter` (`NameCreditCategoryFilter`)None
    * `sort` (`NameCreditSort`)None
    '''

    credit_summary = sgqlc.types.Field(NameCreditSummary, graphql_name='creditSummary')

    credits = sgqlc.types.Field('NameCreditConnection', graphql_name='credits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NameCreditsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(NameCreditSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NameCreditsFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `sort` (`NameCreditSort`)None
    '''

    death_cause = sgqlc.types.Field(DisplayableNameDeathCause, graphql_name='deathCause')

    death_date = sgqlc.types.Field(DisplayableDate, graphql_name='deathDate')

    death_location = sgqlc.types.Field(DisplayableLocation, graphql_name='deathLocation')

    death_status = sgqlc.types.Field(NameDeathStatus, graphql_name='deathStatus')

    demographic_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DemographicDataItem)), graphql_name='demographicData', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DemographicDataFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `filter` (`DemographicDataFilter`)None
    * `limit` (`Int`)None
    '''

    disambiguator = sgqlc.types.Field(Disambiguation, graphql_name='disambiguator')

    engagement_statistics = sgqlc.types.Field(EngagementStatistics, graphql_name='engagementStatistics')

    experimental_credit_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExperimentalNameCreditCategoryWithCredits)), graphql_name='experimental_creditCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NameCreditCategoryFilter, graphql_name='filter', default=None)),
        ('sort', sgqlc.types.Arg(NameCreditSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `filter` (`NameCreditCategoryFilter`)None
    * `sort` (`NameCreditSort`)None
    '''

    experimental_credits = sgqlc.types.Field(ExperimentalNameCreditConnection, graphql_name='experimental_credits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NameCreditsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(NameCreditSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NameCreditsFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `sort` (`NameCreditSort`)None
    '''

    experimental_resume = sgqlc.types.Field(Experimental_Resume, graphql_name='experimental_resume')

    experimental_track_notification_preferences = sgqlc.types.Field(Experimental_TrackNotificationPreferences, graphql_name='experimental_trackNotificationPreferences')

    external_link_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExternalLinkCategoryWithExternalLinks)), graphql_name='externalLinkCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ExternalLinksFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`ExternalLinksFilter`)None
    '''

    external_links = sgqlc.types.Field(ExternalLinkConnection, graphql_name='externalLinks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ExternalLinksFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ExternalLinksFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    featured_external_link_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExternalLinkCategoryWithFeaturedExternalLinks)), graphql_name='featuredExternalLinkCategories')

    featured_polls = sgqlc.types.Field('PollsConnection', graphql_name='featuredPolls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    height = sgqlc.types.Field('NameHeight', graphql_name='height', args=sgqlc.types.ArgDict((
        ('unit', sgqlc.types.Arg(LengthUnit, graphql_name='unit', default='CENTIMETER')),
))
    )
    '''Arguments:

    * `unit` (`LengthUnit`)None (default: `CENTIMETER`)
    '''

    image_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImageTypeWithImages)), graphql_name='imageTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NameImagesFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`NameImagesFilter`)None
    '''

    image_upload_link = sgqlc.types.Field(ContributionLink, graphql_name='imageUploadLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    images = sgqlc.types.Field(ImageConnection, graphql_name='images', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('bust', sgqlc.types.Arg(String, graphql_name='bust', default=None)),
        ('filter', sgqlc.types.Arg(NameImagesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `bust` (`String`)None
    * `filter` (`NameImagesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    is_claimed = sgqlc.types.Field(Boolean, graphql_name='isClaimed')

    known_for = sgqlc.types.Field('NameKnownForConnection', graphql_name='knownFor', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    managed_data = sgqlc.types.Field(NameManagedData, graphql_name='managedData')

    meta = sgqlc.types.Field('NameMeta', graphql_name='meta')

    meter_ranking = sgqlc.types.Field('NameMeterRanking', graphql_name='meterRanking')

    meter_ranking_history = sgqlc.types.Field('NameMeterRankingHistory', graphql_name='meterRankingHistory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(NameMeterRankingHistoryInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`NameMeterRankingHistoryInput`)None
    '''

    more_like_this_names = sgqlc.types.Field(MoreLikeThisNameConnection, graphql_name='moreLikeThisNames', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    name_text = sgqlc.types.Field(NameText, graphql_name='nameText')

    news = sgqlc.types.Field(NewsConnection, graphql_name='news', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int!`)None
    '''

    nick_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NickName')), graphql_name='nickNames', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    nominations = sgqlc.types.Field('NominationConnection', graphql_name='nominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(NominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`NominationsSort`)None
    '''

    other_works = sgqlc.types.Field('NameOtherWorkConnection', graphql_name='otherWorks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    prestigious_award_summary = sgqlc.types.Field(PrestigiousAwardSummary, graphql_name='prestigiousAwardSummary')

    primary_image = sgqlc.types.Field(Image, graphql_name='primaryImage')

    primary_professions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PrimaryProfession)), graphql_name='primaryProfessions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    primary_videos = sgqlc.types.Field('VideoConnection', graphql_name='primaryVideos', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    professions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameProfession)), graphql_name='professions', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    publicity_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PublicityCategoryWithListings)), graphql_name='publicityCategories')

    publicity_listings = sgqlc.types.Field('PublicityListingConnection', graphql_name='publicityListings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(PublicityListingsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`PublicityListingsFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    quotes = sgqlc.types.Field('NameQuoteConnection', graphql_name='quotes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    related_lists = sgqlc.types.Field(ListCollectionConnection, graphql_name='relatedLists', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    relations = sgqlc.types.Field('NameRelationsConnection', graphql_name='relations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NameRelationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NameRelationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    search_indexing = sgqlc.types.Field(NameSearchIndexing, graphql_name='searchIndexing')

    self_verified_data = sgqlc.types.Field(SelfVerifiedNameData, graphql_name='selfVerifiedData')

    shared_names = sgqlc.types.Field(SharedNamesResult, graphql_name='sharedNames', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(SharedNamesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SharedNamesInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`SharedNamesFilter`)None
    * `first` (`Int`)None
    * `input` (`SharedNamesInput!`)None
    '''

    shared_titles = sgqlc.types.Field('SharedTitlesConnection', graphql_name='sharedTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SharedTitlesInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int`)None
    * `input` (`SharedTitlesInput!`)None
    '''

    spouses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NameSpouse')), graphql_name='spouses')

    title_salaries = sgqlc.types.Field('SalaryConnection', graphql_name='titleSalaries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    trademarks = sgqlc.types.Field('TrademarkConnection', graphql_name='trademarks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    trivia = sgqlc.types.Field('NameTriviaConnection', graphql_name='trivia', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    user_selected_professions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NameProfession)), graphql_name='userSelectedProfessions')

    vanity_url = sgqlc.types.Field('VanityUrl', graphql_name='vanityUrl')

    video_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoTypeWithVideos)), graphql_name='videoTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(VideosQueryFilter, graphql_name='filter', default=None)),
        ('sort', sgqlc.types.Arg(VideoSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `filter` (`VideosQueryFilter`)None
    * `sort` (`VideoSort`)None
    '''

    videos = sgqlc.types.Field('VideoConnection', graphql_name='videos', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(VideosQueryFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(VideoSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`VideosQueryFilter`)None
    * `first` (`Int!`)None
    * `sort` (`VideoSort`)None
    '''



class NameAka(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class NameAkaConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameAkaEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameAka), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameBio(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('author', 'category', 'id', 'language', 'text')
    author = sgqlc.types.Field(Markdown, graphql_name='author')

    category = sgqlc.types.Field('NameBioCategory', graphql_name='category')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class NameBioCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class NameBioEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameBio), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameBiosConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameCreditCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class NameCreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('order_by', 'restriction', 'total')
    order_by = sgqlc.types.Field(CreditsOrderedBy, graphql_name='orderBy')

    restriction = sgqlc.types.Field(CreditRestriction, graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameFacetConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameFacetEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position', 'total')
    node = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameHeight(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('measurement',)
    measurement = sgqlc.types.Field(sgqlc.types.non_null(LengthMeasurement), graphql_name='measurement')



class NameKnownForConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('NameKnownForRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameKnownForEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameKnownFor), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameKnownForRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class NameListItemSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facet', 'total')
    facet = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SearchFacet')), graphql_name='facet', args=sgqlc.types.ArgDict((
        ('facet_field', sgqlc.types.Arg(sgqlc.types.non_null(NameFacetField), graphql_name='facetField', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `facet_field` (`NameFacetField!`)None
    * `limit` (`Int`)None
    '''

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameListItemSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('name', 'node')
    name = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='name')

    node = sgqlc.types.Field(sgqlc.types.non_null(ListItemSearchNode), graphql_name='node')



class NameMeta(sgqlc.types.Type, Meta):
    __schema__ = model
    __field_names__ = ()


class NameMeterRanking(sgqlc.types.Type, MeterRanking):
    __schema__ = model
    __field_names__ = ()


class NameMeterRankingHistory(sgqlc.types.Type, MeterRankingHistory):
    __schema__ = model
    __field_names__ = ()


class NameOtherWork(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('category', 'from_date', 'id', 'text', 'to_date')
    category = sgqlc.types.Field('NameOtherWorkCategory', graphql_name='category')

    from_date = sgqlc.types.Field(Date, graphql_name='fromDate')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')

    to_date = sgqlc.types.Field(Date, graphql_name='toDate')



class NameOtherWorkCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class NameOtherWorkConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameOtherWorkEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameOtherWork), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NamePersonalLocation(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='latitude')

    longitude = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='longitude')



class NameQuote(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('id', 'language', 'text')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    language = sgqlc.types.Field(DisplayableLanguage, graphql_name='language')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class NameQuoteConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameQuoteEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameQuote), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameRecommendationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class NameRecommendationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(NameRecommendation), graphql_name='node')



class NameRelationType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class NameRelationsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameRelationsEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameRelation), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class NameSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='node')



class NameSpouse(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'current', 'spouse', 'time_range')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SpouseAttributes')), graphql_name='attributes')

    current = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='current')

    spouse = sgqlc.types.Field(SpouseName, graphql_name='spouse')

    time_range = sgqlc.types.Field(DisplayableSpouseTimeRange, graphql_name='timeRange')



class NameToTitleAttachmentConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameToTitleAttachmentEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(NameToTitleAttachment), graphql_name='node')



class NameTrackRecommendationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NameTrackRecommendationsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameTrivia(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('date', 'id', 'interest_score', 'text')
    date = sgqlc.types.Field(Date, graphql_name='date')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class NameTriviaConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NameTriviaEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NameTrivia), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NegativeFormat(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'negative_format')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    negative_format = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='negativeFormat')



class NewsLink(sgqlc.types.Type, Link):
    __schema__ = model
    __field_names__ = ()


class NewsRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class NewsSourceIconImage(sgqlc.types.Type, ImageObject):
    __schema__ = model
    __field_names__ = ()


class NickName(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class NominationAward(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('nomination_categories',)
    nomination_categories = sgqlc.types.Field('NominationsWithCategoryConnection', graphql_name='nominationCategories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''



class NominationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NominationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Nomination), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class NominationEventName(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class NominationsWithCategoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class NominationsWithCategoryEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(NominationsWithCategory), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class OpeningWeekendBoxOfficeGrossConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class OpeningWeekendBoxOfficeGrossEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(OpeningWeekendGross), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ParentsGuideCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ParentsGuideConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ParentsGuideEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ParentsGuideItem), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class PersonalizedSuggestedVideosConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class PersonalizedSuggestedVideosEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Video), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class PlotConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('PlotRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class PlotEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Plot), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class PlotRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ()


class PollAnswerEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(PollAnswer), graphql_name='node')



class PollAnswersConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class PollEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Poll), graphql_name='node')



class PollsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class PrintedFormat(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'printed_format')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    printed_format = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='printedFormat')



class Process(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'process')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    process = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='process')



class ProductionAnnouncementComment(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ProductionDatesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ProductionDatesEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ProductionDate), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ProductionStage(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ProductionStatus(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ProductionStatusHistoryComment(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ProductionStatusHistoryRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class Profession(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class PublicityListingCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class PublicityListingConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class PublicityListingEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(PublicityListingType), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class QuestionConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('contribution_link', 'supported_filters')
    contribution_link = sgqlc.types.Field(sgqlc.types.non_null(ContributionQuestionsLink), graphql_name='contributionLink')

    supported_filters = sgqlc.types.Field(sgqlc.types.non_null(SupportedQuestionFilters), graphql_name='supportedFilters')



class QuestionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Question), graphql_name='node')



class RankedLifetimeBoxOfficeGrossConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class RankedLifetimeBoxOfficeGrossEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(RankedLifetimeBoxOfficeGross), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class RatingsBody(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class RatingsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class RatingsEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(RatingsResult), graphql_name='node')



class RatingsPrivacy(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('setting',)
    setting = sgqlc.types.Field(sgqlc.types.non_null(RatingsPrivacySetting), graphql_name='setting')



class Reaction(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('reaction_id',)
    reaction_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='reactionId')



class RecentlyViewedConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('ref_tag',)
    ref_tag = sgqlc.types.Field(RefTag, graphql_name='refTag')



class RecentlyViewedEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('RecentlyViewedItem'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class RelationName(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('name', 'name_text')
    name = sgqlc.types.Field(Name, graphql_name='name')

    name_text = sgqlc.types.Field(String, graphql_name='nameText')



class ReleaseDate(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'country', 'day', 'month', 'restriction', 'year')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute)), graphql_name='attributes')

    country = sgqlc.types.Field(LocalizedDisplayableCountry, graphql_name='country')

    day = sgqlc.types.Field(Int, graphql_name='day')

    month = sgqlc.types.Field(Int, graphql_name='month')

    restriction = sgqlc.types.Field('ReleaseDateRestriction', graphql_name='restriction')

    year = sgqlc.types.Field(Int, graphql_name='year')



class ReleaseDateConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ReleaseDateEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(ReleaseDate), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ReleaseDateRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ()


class ReviewEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Review), graphql_name='node')



class ReviewsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Runtime(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes', 'country', 'id', 'seconds')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')

    country = sgqlc.types.Field(DisplayableCountry, graphql_name='country')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    seconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seconds')



class RuntimeConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class RuntimeEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Runtime), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Salary(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('amount', 'attributes', 'id', 'title')
    amount = sgqlc.types.Field(Money, graphql_name='amount')

    attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute)), graphql_name='attributes')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    title = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='title')



class SalaryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SalaryEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Salary), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class ScreeningDateTime(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('date_time',)
    date_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='dateTime')



class SearchAwardCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class SearchAwardEvent(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('award_categories',)
    award_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SearchAwardCategory)), graphql_name='awardCategories')



class SearchFacet(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('filter_id', 'total')
    filter_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='filterId')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SeasonValueDisplayableProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()


class SelfVerifiedNameAttributeValue(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class SelfVerifiedNameAwardConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SelfVerifiedNameAwardEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(SelfVerifiedNameAward), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SelfVerifiedNameCreditConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SelfVerifiedNameCreditEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(SelfVerifiedNameCredit), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SelfVerifiedNameCreditType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class SelfVerifiedNameEducationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(SelfVerifiedNameEducation, graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SelfVerifiedNameEducationalHistoryConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SelfVerifiedNameReferenceConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SelfVerifiedNameReferenceEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(SelfVerifiedNameReference), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SelfVerifiedNameTrainingEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(SelfVerifiedNameTraining, graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SelfVerifiedResumeCustomSectionConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SelfVerifiedResumeCustomSectionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(SelfVerifiedResumeCustomSection), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SeverityLevel(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('vote_type', 'voted_for')
    vote_type = sgqlc.types.Field(sgqlc.types.non_null(SeverityVote), graphql_name='voteType')

    voted_for = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='votedFor')



class SharedNameEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(SharedNameItem), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SharedNamesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SharedTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SharedTitlesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class ShowtimeScreeningType(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class ShowtimesTitleConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class ShowtimesTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('Title'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SoundMix(sgqlc.types.Type, DisplayableConcept, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('attributes',)
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DisplayableAttribute))), graphql_name='attributes')



class SoundtrackConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('SoundtrackRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class SoundtrackEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null('Track'), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class SoundtrackRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class SpokenLanguage(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class SpouseAttributes(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class StreamingTitleConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class StreamingTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(StreamingTitle), graphql_name='node')



class SuggestionSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class SuggestionSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null('SuggestionSearchItem'), graphql_name='node')



class SuggestionSearchItem(sgqlc.types.Type, DisplayableSearchResult):
    __schema__ = model
    __field_names__ = ('const_id', 'id', 'rank', 'ref_tag_fragment', 'title_type_id', 'top_videos', 'url', 'video_count')
    const_id = sgqlc.types.Field(ID, graphql_name='constId')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    rank = sgqlc.types.Field(Int, graphql_name='rank')

    ref_tag_fragment = sgqlc.types.Field(String, graphql_name='refTagFragment')

    title_type_id = sgqlc.types.Field(String, graphql_name='titleTypeId')

    top_videos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoMedia)), graphql_name='topVideos')

    url = sgqlc.types.Field(String, graphql_name='url')

    video_count = sgqlc.types.Field(Int, graphql_name='videoCount')



class Tagline(sgqlc.types.Type, HasDisplayableProperty):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')



class TaglineConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TaglineEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Tagline), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TechnicalSpecificationsRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class Title(sgqlc.types.Type, PrimaryConst):
    __schema__ = model
    __field_names__ = ('aggregate_ratings_breakdown', 'akas', 'alexa_top_questions', 'alternate_versions', 'amazon_music_albums', 'award_nominations', 'can_rate', 'canonical_url', 'certificate', 'certificates', 'cinema_showtimes_by_screening_type', 'company_credit_categories', 'company_credits', 'connection_categories', 'connections', 'contribution_questions', 'countries_of_origin', 'crazy_credits', 'credit_categories', 'credits', 'engagement_statistics', 'episodes', 'experimental_add_faq_call_to_action', 'experimental_core_catalog', 'experimental_credits', 'external_link_categories', 'external_links', 'faqs', 'featured_polls', 'featured_reviews', 'filming_dates', 'filming_locations', 'goof_categories', 'goofs', 'image_types', 'image_upload_link', 'images', 'interests', 'is_adult', 'is_wgaverified', 'keyword_item_categories', 'keywords', 'latest_trailer', 'latest_trailer_webview_player', 'lifetime_gross', 'meta', 'metacritic', 'meter_ranking', 'more_like_this_titles', 'news', 'nominations', 'notification_preferences', 'opening_weekend_gross', 'opening_weekend_grosses', 'original_title_text', 'parents_guide', 'parents_guide_contribution_link', 'plot', 'plot_contribution_link', 'plots', 'prestigious_award_summary', 'primary_image', 'primary_videos', 'primary_watch_option', 'principal_credits', 'production_budget', 'production_dates', 'production_status', 'quotes', 'ranked_lifetime_gross', 'ranked_lifetime_grosses', 'ratings_summary', 'related_interests', 'related_lists', 'release_date', 'release_dates', 'release_year', 'review_contribution_link', 'reviews', 'runtime', 'runtimes', 'series', 'soundtrack', 'spoken_languages', 'taglines', 'technical_specifications', 'title_genres', 'title_text', 'title_type', 'trivia', 'trivia_categories', 'trivia_contribution_link', 'user_rating', 'video_strip', 'video_types', 'watch_option', 'watch_options_by_category')
    aggregate_ratings_breakdown = sgqlc.types.Field(AggregateRatingsBreakdown, graphql_name='aggregateRatingsBreakdown')

    akas = sgqlc.types.Field(AkaConnection, graphql_name='akas', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(AkaFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(AkaSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`AkaFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `sort` (`AkaSort`)None
    '''

    alexa_top_questions = sgqlc.types.Field(AlexaQuestionConnection, graphql_name='alexaTopQuestions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    alternate_versions = sgqlc.types.Field(AlternateVersionConnection, graphql_name='alternateVersions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    amazon_music_albums = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AmazonMusicProduct)), graphql_name='amazonMusicAlbums', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    award_nominations = sgqlc.types.Field(AwardNominationConnection, graphql_name='awardNominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(AwardNominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(AwardNominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`AwardNominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`AwardNominationsSort`)None
    '''

    can_rate = sgqlc.types.Field(CanRate, graphql_name='canRate')

    canonical_url = sgqlc.types.Field(String, graphql_name='canonicalUrl')

    certificate = sgqlc.types.Field(Certificate, graphql_name='certificate')

    certificates = sgqlc.types.Field(CertificatesConnection, graphql_name='certificates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(CertificatesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`CertificatesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    cinema_showtimes_by_screening_type = sgqlc.types.Field('TitleCinemaShowtimesByScreeningTypeConnection', graphql_name='cinemaShowtimesByScreeningType', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(TitleCinemaShowtimesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`TitleCinemaShowtimesFilter`)None
    * `first` (`Int`)None
    '''

    company_credit_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyCreditCategoryWithCompanyCredits)), graphql_name='companyCreditCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyCreditsFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`CompanyCreditsFilter`)None
    '''

    company_credits = sgqlc.types.Field(CompanyCreditConnection, graphql_name='companyCredits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(CompanyCreditsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`CompanyCreditsFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    connection_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConnectionCategoryWithConnections)), graphql_name='connectionCategories')

    connections = sgqlc.types.Field('TitleConnectionConnection', graphql_name='connections', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ConnectionsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ConnectionsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    contribution_questions = sgqlc.types.Field(QuestionConnection, graphql_name='contributionQuestions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(QuestionsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `filter` (`QuestionsFilter`)None
    * `first` (`Int`)None
    '''

    countries_of_origin = sgqlc.types.Field(CountriesOfOrigin, graphql_name='countriesOfOrigin')

    crazy_credits = sgqlc.types.Field(CrazyCreditConnection, graphql_name='crazyCredits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    credit_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleCreditCategoryWithCredits)), graphql_name='creditCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TitleCreditCategoryWithCreditsFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`TitleCreditCategoryWithCreditsFilter`)None
    '''

    credits = sgqlc.types.Field(CreditConnection, graphql_name='credits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(TitleCreditsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(TitleCreditSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`TitleCreditsFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `sort` (`TitleCreditSort`)None
    '''

    engagement_statistics = sgqlc.types.Field(EngagementStatistics, graphql_name='engagementStatistics')

    episodes = sgqlc.types.Field(Episodes, graphql_name='episodes')

    experimental_add_faq_call_to_action = sgqlc.types.Field(Experimental_UIWorkflowCTA, graphql_name='experimental_addFaqCallToAction')

    experimental_core_catalog = sgqlc.types.Field(TitleCoreCatalog, graphql_name='experimental_coreCatalog')

    experimental_credits = sgqlc.types.Field(ExperimentalCreditConnection, graphql_name='experimental_credits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ExperimentalTitleCreditsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(TitleCreditSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ExperimentalTitleCreditsFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `sort` (`TitleCreditSort`)None
    '''

    external_link_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExternalLinkCategoryWithExternalLinks)), graphql_name='externalLinkCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ExternalLinksFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`ExternalLinksFilter`)None
    '''

    external_links = sgqlc.types.Field(ExternalLinkConnection, graphql_name='externalLinks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(ExternalLinksFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`ExternalLinksFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    faqs = sgqlc.types.Field(FaqConnection, graphql_name='faqs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(FaqsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`FaqsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    featured_polls = sgqlc.types.Field(PollsConnection, graphql_name='featuredPolls', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    featured_reviews = sgqlc.types.Field(ReviewsConnection, graphql_name='featuredReviews', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int!`)None
    '''

    filming_dates = sgqlc.types.Field(FilmingDatesConnection, graphql_name='filmingDates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    filming_locations = sgqlc.types.Field(FilmingLocationConnection, graphql_name='filmingLocations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    goof_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GoofCategoryWithGoofs)), graphql_name='goofCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(GoofCategoryWithGoofsFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`GoofCategoryWithGoofsFilter`)None
    '''

    goofs = sgqlc.types.Field(GoofConnection, graphql_name='goofs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(GoofsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`GoofsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    image_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImageTypeWithImages)), graphql_name='imageTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ImagesFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`ImagesFilter`)None
    '''

    image_upload_link = sgqlc.types.Field(ContributionLink, graphql_name='imageUploadLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    images = sgqlc.types.Field(ImageConnection, graphql_name='images', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('bust', sgqlc.types.Arg(String, graphql_name='bust', default=None)),
        ('filter', sgqlc.types.Arg(ImagesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `bust` (`String`)None
    * `filter` (`ImagesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    interests = sgqlc.types.Field(InterestConnection, graphql_name='interests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    is_adult = sgqlc.types.Field(Boolean, graphql_name='isAdult')

    is_wgaverified = sgqlc.types.Field(Boolean, graphql_name='isWGAVerified')

    keyword_item_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TitleKeywordItemCategoryWithKeywords)), graphql_name='keywordItemCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TitleKeywordItemCategoriesFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`TitleKeywordItemCategoriesFilter`)None
    '''

    keywords = sgqlc.types.Field('TitleKeywordConnection', graphql_name='keywords', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(TitleKeywordsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`TitleKeywordsSort`)None
    '''

    latest_trailer = sgqlc.types.Field(Video, graphql_name='latestTrailer')

    latest_trailer_webview_player = sgqlc.types.Field(WebviewVideoPlayer, graphql_name='latestTrailerWebviewPlayer', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(LatestTrailerFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`LatestTrailerFilter`)None
    '''

    lifetime_gross = sgqlc.types.Field(BoxOfficeGross, graphql_name='lifetimeGross', args=sgqlc.types.ArgDict((
        ('box_office_area', sgqlc.types.Arg(sgqlc.types.non_null(BoxOfficeArea), graphql_name='boxOfficeArea', default=None)),
))
    )
    '''Arguments:

    * `box_office_area` (`BoxOfficeArea!`)None
    '''

    meta = sgqlc.types.Field('TitleMeta', graphql_name='meta')

    metacritic = sgqlc.types.Field(Metacritic, graphql_name='metacritic')

    meter_ranking = sgqlc.types.Field('TitleMeterRanking', graphql_name='meterRanking', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(TitleMeterRankingInput, graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`TitleMeterRankingInput`)None
    '''

    more_like_this_titles = sgqlc.types.Field(MoreLikeThisConnection, graphql_name='moreLikeThisTitles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    news = sgqlc.types.Field(NewsConnection, graphql_name='news', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `first` (`Int!`)None
    '''

    nominations = sgqlc.types.Field(NominationConnection, graphql_name='nominations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(NominationsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sort', sgqlc.types.Arg(NominationsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`NominationsFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    * `sort` (`NominationsSort`)None
    '''

    notification_preferences = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Experimental_NotificationPreference)), graphql_name='notificationPreferences')

    opening_weekend_gross = sgqlc.types.Field(OpeningWeekendGross, graphql_name='openingWeekendGross', args=sgqlc.types.ArgDict((
        ('box_office_area', sgqlc.types.Arg(sgqlc.types.non_null(BoxOfficeArea), graphql_name='boxOfficeArea', default=None)),
))
    )
    '''Arguments:

    * `box_office_area` (`BoxOfficeArea!`)None
    '''

    opening_weekend_grosses = sgqlc.types.Field(OpeningWeekendBoxOfficeGrossConnection, graphql_name='openingWeekendGrosses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(OpeningWeekendBoxOfficeGrossFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`OpeningWeekendBoxOfficeGrossFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    original_title_text = sgqlc.types.Field(TitleText, graphql_name='originalTitleText')

    parents_guide = sgqlc.types.Field(ParentsGuide, graphql_name='parentsGuide')

    parents_guide_contribution_link = sgqlc.types.Field(ContributionLink, graphql_name='parentsGuideContributionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    plot = sgqlc.types.Field(Plot, graphql_name='plot')

    plot_contribution_link = sgqlc.types.Field(ContributionLink, graphql_name='plotContributionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    plots = sgqlc.types.Field(PlotConnection, graphql_name='plots', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(FilterPlots, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('include_all_locales', sgqlc.types.Arg(Boolean, graphql_name='includeAllLocales', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`FilterPlots`)None
    * `first` (`Int`)None
    * `include_all_locales` (`Boolean`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    prestigious_award_summary = sgqlc.types.Field(PrestigiousAwardSummary, graphql_name='prestigiousAwardSummary')

    primary_image = sgqlc.types.Field(Image, graphql_name='primaryImage')

    primary_videos = sgqlc.types.Field('VideoConnection', graphql_name='primaryVideos', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `first` (`Int`)None
    '''

    primary_watch_option = sgqlc.types.Field(PrimaryWatchOption, graphql_name='primaryWatchOption', args=sgqlc.types.ArgDict((
        ('location', sgqlc.types.Arg(WatchOptionsLocation, graphql_name='location', default=None)),
        ('promoted_provider', sgqlc.types.Arg(String, graphql_name='promotedProvider', default=None)),
))
    )
    '''Arguments:

    * `location` (`WatchOptionsLocation`)None
    * `promoted_provider` (`String`)None
    '''

    principal_credits = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PrincipalCreditsForCategory)), graphql_name='principalCredits', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PrincipalCreditsFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`PrincipalCreditsFilter`)None
    '''

    production_budget = sgqlc.types.Field(ProductionBudget, graphql_name='productionBudget')

    production_dates = sgqlc.types.Field(ProductionDatesConnection, graphql_name='productionDates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    production_status = sgqlc.types.Field(ProductionStatusDetails, graphql_name='productionStatus')

    quotes = sgqlc.types.Field('TitleQuoteConnection', graphql_name='quotes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(TitleQuotesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`TitleQuotesFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    ranked_lifetime_gross = sgqlc.types.Field(RankedLifetimeBoxOfficeGross, graphql_name='rankedLifetimeGross', args=sgqlc.types.ArgDict((
        ('box_office_area', sgqlc.types.Arg(sgqlc.types.non_null(BoxOfficeArea), graphql_name='boxOfficeArea', default=None)),
))
    )
    '''Arguments:

    * `box_office_area` (`BoxOfficeArea!`)None
    '''

    ranked_lifetime_grosses = sgqlc.types.Field(RankedLifetimeBoxOfficeGrossConnection, graphql_name='rankedLifetimeGrosses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(RankedLifetimeBoxOfficeGrossFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`RankedLifetimeBoxOfficeGrossFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    ratings_summary = sgqlc.types.Field(RatingsSummary, graphql_name='ratingsSummary')

    related_interests = sgqlc.types.Field(InterestConnection, graphql_name='relatedInterests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    related_lists = sgqlc.types.Field(ListCollectionConnection, graphql_name='relatedLists', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `first` (`Int!`)None
    '''

    release_date = sgqlc.types.Field(ReleaseDate, graphql_name='releaseDate')

    release_dates = sgqlc.types.Field(ReleaseDateConnection, graphql_name='releaseDates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(TitleReleaseDatesFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`TitleReleaseDatesFilter`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    release_year = sgqlc.types.Field(YearRange, graphql_name='releaseYear')

    review_contribution_link = sgqlc.types.Field(ContributionLink, graphql_name='reviewContributionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    reviews = sgqlc.types.Field(ReviewsConnection, graphql_name='reviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(ReviewsFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(ReviewsSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`ReviewsFilter`)None
    * `first` (`Int!`)None
    * `sort` (`ReviewsSort`)None
    '''

    runtime = sgqlc.types.Field(Runtime, graphql_name='runtime')

    runtimes = sgqlc.types.Field(RuntimeConnection, graphql_name='runtimes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    series = sgqlc.types.Field(Series, graphql_name='series')

    soundtrack = sgqlc.types.Field(SoundtrackConnection, graphql_name='soundtrack', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    spoken_languages = sgqlc.types.Field(SpokenLanguages, graphql_name='spokenLanguages')

    taglines = sgqlc.types.Field(TaglineConnection, graphql_name='taglines', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    technical_specifications = sgqlc.types.Field(TechnicalSpecifications, graphql_name='technicalSpecifications', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TechnicalSpecificationsFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`TechnicalSpecificationsFilter`)None
    '''

    title_genres = sgqlc.types.Field(TitleGenres, graphql_name='titleGenres')

    title_text = sgqlc.types.Field(TitleText, graphql_name='titleText')

    title_type = sgqlc.types.Field('TitleType', graphql_name='titleType')

    trivia = sgqlc.types.Field('TriviaConnection', graphql_name='trivia', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(ID, graphql_name='before', default=None)),
        ('filter', sgqlc.types.Arg(TriviaFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('jump_to', sgqlc.types.Arg(ID, graphql_name='jumpTo', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `before` (`ID`)None
    * `filter` (`TriviaFilter`)None
    * `first` (`Int`)None
    * `jump_to` (`ID`)None
    * `last` (`Int`)None
    '''

    trivia_categories = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TriviaCategoryWithTrivia)), graphql_name='triviaCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TriviaCategoryWithTriviaFilter, graphql_name='filter', default=None)),
))
    )
    '''Arguments:

    * `filter` (`TriviaCategoryWithTriviaFilter`)None
    '''

    trivia_contribution_link = sgqlc.types.Field(ContributionLink, graphql_name='triviaContributionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    user_rating = sgqlc.types.Field(Rating, graphql_name='userRating', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(ID, graphql_name='userId', default=None)),
))
    )
    '''Arguments:

    * `user_id` (`ID`)None
    '''

    video_strip = sgqlc.types.Field('VideoConnection', graphql_name='videoStrip', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(ID, graphql_name='after', default=None)),
        ('filter', sgqlc.types.Arg(VideosQueryFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(VideoSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `after` (`ID`)None
    * `filter` (`VideosQueryFilter`)None
    * `first` (`Int`)None
    * `sort` (`VideoSort`)None
    '''

    video_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VideoTypeWithVideos)), graphql_name='videoTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(VideosQueryFilter, graphql_name='filter', default=None)),
        ('sort', sgqlc.types.Arg(VideoSort, graphql_name='sort', default=None)),
))
    )
    '''Arguments:

    * `filter` (`VideosQueryFilter`)None
    * `sort` (`VideoSort`)None
    '''

    watch_option = sgqlc.types.Field(WatchOption, graphql_name='watchOption', args=sgqlc.types.ArgDict((
        ('location', sgqlc.types.Arg(WatchOptionsLocation, graphql_name='location', default=None)),
        ('provider_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='providerId', default=None)),
))
    )
    '''Arguments:

    * `location` (`WatchOptionsLocation`)None
    * `provider_id` (`ID!`)None
    '''

    watch_options_by_category = sgqlc.types.Field(CategorizedWatchOptionsList, graphql_name='watchOptionsByCategory', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('location', sgqlc.types.Arg(WatchOptionsLocation, graphql_name='location', default=None)),
        ('promoted_provider', sgqlc.types.Arg(String, graphql_name='promotedProvider', default=None)),
        ('query_filter', sgqlc.types.Arg(WatchOptionQueryFilter, graphql_name='queryFilter', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    * `location` (`WatchOptionsLocation`)None
    * `promoted_provider` (`String`)None
    * `query_filter` (`WatchOptionQueryFilter`)None
    '''



class TitleChartRankingsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('metadata',)
    metadata = sgqlc.types.Field(sgqlc.types.non_null(TitleChartMetadata), graphql_name='metadata')



class TitleChartRankingsEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleChartRankingsNode), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TitleCinemaShowtimesByScreeningTypeConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleCinemaShowtimesByScreeningTypeEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleCinemaShowtimesByScreeningType), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TitleConnectionCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class TitleConnectionConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleConnectionEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleConnection), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TitleFacetConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleFacetEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position', 'total')
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleGenreRecommendationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class TitleGenreRecommendationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')



class TitleKeywordConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleKeywordEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleKeyword), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TitleKeywordItemCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('item_category_id',)
    item_category_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='itemCategoryId')



class TitleListItemSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facet', 'my_rated_count', 'my_rated_percentage', 'total')
    facet = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SearchFacet)), graphql_name='facet', args=sgqlc.types.ArgDict((
        ('facet_field', sgqlc.types.Arg(sgqlc.types.non_null(TitleFacetField), graphql_name='facetField', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `facet_field` (`TitleFacetField!`)None
    * `limit` (`Int`)None
    '''

    my_rated_count = sgqlc.types.Field(Int, graphql_name='myRatedCount')

    my_rated_percentage = sgqlc.types.Field(LocalizedString, graphql_name='myRatedPercentage')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleListItemSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'title')
    node = sgqlc.types.Field(sgqlc.types.non_null(ListItemSearchNode), graphql_name='node')

    title = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='title')



class TitleMeta(sgqlc.types.Type, Meta):
    __schema__ = model
    __field_names__ = ('restrictions',)
    restrictions = sgqlc.types.Field('TitleMetaRestrictions', graphql_name='restrictions')



class TitleMetaRestrictions(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ()


class TitleMeterRanking(sgqlc.types.Type, MeterRanking):
    __schema__ = model
    __field_names__ = ('meter_type',)
    meter_type = sgqlc.types.Field(TitleMeterType, graphql_name='meterType')



class TitleQuote(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('id', 'interest_score', 'is_spoiler', 'language', 'lines')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    is_spoiler = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSpoiler')

    language = sgqlc.types.Field(sgqlc.types.non_null(DisplayableLanguage), graphql_name='language')

    lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TitleQuoteLine))), graphql_name='lines')



class TitleQuoteConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleQuoteEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleQuote), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TitleRecommendationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class TitleRecommendationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleRecommendation), graphql_name='node')



class TitleSearchConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class TitleSearchEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')



class TitleTrackRecommendationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TitleTrackRecommendationsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TitleTrivia(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('category', 'correction_link', 'id', 'interest_score', 'is_spoiler', 'related_names', 'reporting_link', 'text', 'title', 'trademark')
    category = sgqlc.types.Field(sgqlc.types.non_null('TriviaCategory'), graphql_name='category')

    correction_link = sgqlc.types.Field(ContributionLink, graphql_name='correctionLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    interest_score = sgqlc.types.Field(sgqlc.types.non_null(InterestScore), graphql_name='interestScore')

    is_spoiler = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSpoiler')

    related_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Name)), graphql_name='relatedNames')

    reporting_link = sgqlc.types.Field(ContributionLink, graphql_name='reportingLink', args=sgqlc.types.ArgDict((
        ('contribution_context', sgqlc.types.Arg(sgqlc.types.non_null(ContributionContext), graphql_name='contributionContext', default=None)),
))
    )
    '''Arguments:

    * `contribution_context` (`ContributionContext!`)None
    '''

    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')

    title = sgqlc.types.Field(Title, graphql_name='title')

    trademark = sgqlc.types.Field(Markdown, graphql_name='trademark')



class TitleType(sgqlc.types.Type, HasDisplayableProperty, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('can_have_episodes', 'categories', 'is_episode', 'is_series')
    can_have_episodes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canHaveEpisodes')

    categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TitleTypeCategory'))), graphql_name='categories')

    is_episode = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEpisode')

    is_series = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSeries')



class TitleTypeCategory(sgqlc.types.Type, LocalizedDisplayableConcept):
    __schema__ = model
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(TitleTypeCategoryValue), graphql_name='value')



class TitleWatchlistRecommendationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('ref_tag',)
    ref_tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refTag')



class TitleWatchlistRecommendationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleWatchlistRecommendation), graphql_name='node')



class TopGrossingReleasesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('displayable_box_office_area', 'time_window_end_date', 'time_window_start_date', 'total')
    displayable_box_office_area = sgqlc.types.Field(BoxOfficeAreaType, graphql_name='displayableBoxOfficeArea')

    time_window_end_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='timeWindowEndDate')

    time_window_start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='timeWindowStartDate')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TopGrossingReleasesEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TopGrossingReleasesNode), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TopPicksConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('ref_tag',)
    ref_tag = sgqlc.types.Field(RefTag, graphql_name='refTag')



class TopPicksEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class Track(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('amazon_music_products', 'comments', 'id', 'text')
    amazon_music_products = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AmazonMusicProduct)), graphql_name='amazonMusicProducts', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    comments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Markdown)), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Arguments:

    * `limit` (`Int`)None
    '''

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    text = sgqlc.types.Field(String, graphql_name='text')



class TrackedNameEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TrackedNamesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TrackedTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TrackedTitlesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class Trademark(sgqlc.types.Type, HasDisplayableArticle):
    __schema__ = model
    __field_names__ = ('text',)
    text = sgqlc.types.Field(sgqlc.types.non_null(Markdown), graphql_name='text')



class TrademarkConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TrademarkEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Trademark), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TrendingNameConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class TrendingNameEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(TrendingNameNode), graphql_name='node')



class TrendingTitleConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class TrendingTitleEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(TrendingTitleNode), graphql_name='node')



class TrendingVideoConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class TrendingVideoEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(TrendingVideoNode), graphql_name='node')



class TriviaCategory(sgqlc.types.Type, DisplayableConcept):
    __schema__ = model
    __field_names__ = ()


class TriviaConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('restriction', 'total')
    restriction = sgqlc.types.Field('TriviaRestriction', graphql_name='restriction')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class TriviaEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(TitleTrivia), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class TriviaRestriction(sgqlc.types.Type, ContentRestriction):
    __schema__ = model
    __field_names__ = ('unrestricted_total',)
    unrestricted_total = sgqlc.types.Field(Int, graphql_name='unrestrictedTotal')



class TwitterLink(sgqlc.types.Type, Link):
    __schema__ = model
    __field_names__ = ('username',)
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')



class UserInterestsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class VanityUrl(sgqlc.types.Type, Link):
    __schema__ = model
    __field_names__ = ('name', 'url_path')
    name = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='name')

    url_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='urlPath')



class VideoConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('facets', 'total')
    facets = sgqlc.types.Field(VideoFacets, graphql_name='facets')

    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class VideoEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Video), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class VideoNameRelationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class VideoNameRelationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class VideoRecommendationsConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class VideoRecommendationsItemsEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null('VideoRecommendationsItem'), graphql_name='node')



class VideoTitleRelationConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class VideoTitleRelationEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node', 'position')
    node = sgqlc.types.Field(sgqlc.types.non_null(Title), graphql_name='node')

    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')



class VideoTypesConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')



class WatchProviderConnection(sgqlc.types.relay.Connection, Connection):
    __schema__ = model
    __field_names__ = ()


class WatchProviderEdge(sgqlc.types.Type, Edge):
    __schema__ = model
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(WatchProvider), graphql_name='node')



class YearDisplayableProperty(sgqlc.types.Type, DisplayableProperty):
    __schema__ = model
    __field_names__ = ()



########################################################################
# Unions
########################################################################
class AnswerItem(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Image, Name, Title)


class AwardedEntities(sgqlc.types.Union):
    __schema__ = model
    __types__ = (AwardedNames, AwardedTitles)


class Entity(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Name, Title)


class Experimental_UIWorkflowElement(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Experimental_UIWorkflowCheckboxFormElement, Experimental_UIWorkflowFeedbackDisplayElement, Experimental_UIWorkflowFeedbackFormElement, Experimental_UIWorkflowMarkdownDisplayElement, Experimental_UIWorkflowRadioGroupFormElement, Experimental_UIWorkflowTextAreaFormElement, Experimental_UIWorkflowTextFormElement)


class Experimental_UIWorkflowFeedbackElement(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Experimental_UIWorkflowFeedbackDisplayElement, Experimental_UIWorkflowFeedbackFormElement)


class Experimental_UIWorkflowGlobalMenuItem(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Experimental_UIWorkflowGlobalMenuItemLink,)


class Experimental_UIWorkflowSubject(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Company, Experimental_UIWorkflowNewSubject, Name, Title)


class ListItem(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Image, Name, Title, Video)


class MainSearchEntity(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Company, Interest, Keyword, Name, Title)


class MarkdownEntity(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Company, Name, Title)


class NewsEntity(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Company, Name, Title)


class RecentlyViewedItem(sgqlc.types.Union):
    __schema__ = model
    __types__ = (Name, Title)


class VideoRecommendationsItem(sgqlc.types.Union):
    __schema__ = model
    __types__ = (VideoRecommendationsAdItem, VideoRecommendationsVideoItem)



########################################################################
# Schema Entry Points
########################################################################
model.query_type = Query
model.mutation_type = None
model.subscription_type = None

