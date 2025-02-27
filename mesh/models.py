from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Literal
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class BaseSchema(BaseModel):
    pass

class Gender(Enum):
    male = 'male'
    female = 'female'

class IdentifyableBase(BaseSchema):
    id: int | None = None

class NamedBase(IdentifyableBase):
    name: str | None = Field(default=None)

class GlobalNamedBase(BaseSchema):
    global_id: int | None = None
    name: str | None = None

class ProfileType(Enum):
    student = 'student'
    teacher = 'teacher'

class UserInfoBase(IdentifyableBase):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    snils: str | None = None
    phone: int | str | None = Field(default=None, alias='phone_number')

class UserInfoBase2(UserInfoBase):
    user_id: int | None = None
    gender: Gender | None = Field(default=None, alias='sex')
    date_of_birth: datetime | None = Field(default=None, alias='birth_date')

# region Config

class ConfigSchema(BaseSchema):
    model_config = ConfigDict(alias_generator=str.upper)

class ExternalLinks(ConfigSchema):
    eais_oko_url: str | None = None
    cashless_payment_for_meals_url: str | None = None
    participation_in_olympiads_url: str | None = None
    results_past_olympiads_url: str | None = None

class ApiURLs(ConfigSchema):
    api_acl: str | None = None
    api_ej_core_family: str | None = None
    api_ej_report_family: str | None = None
    api_additional_education: str | None = None
    api_ej_plan_family: str | None = None
    api_ej_rating: str | None = None
    api_ej_ec_family: str | None = None
    api_ej_organizer_family: str | None = None
    api_ej_partners: str | None = None
    api_certificates_family: str | None = None
    api_nsi_dictionaries: str | None = None
    api_family_web: str | None = None
    api_family_materials: str | None = None
    api_family_ispp: str | None = None
    api_persondata: str | None = None
    api_sfp_service: str | None = None
    api_claims: str | None = None
    api_consents: str | None = None
    api_circles: str | None = None
    api_materials: str | None = None
    api_lib_search: str | None = None
    api_lib_cms: str | None = None
    api_eventcalendar: str | None = None
    api_usersettings: str | None = None
    api_lrs: str | None = None
    api_exam: str | None = None
    api_projects_core: str | None = None
    api_tasting: str | None = None
    api_knowledge_skill: str | None = None
    api_passport_family: str | None = None
    api_event_cover: str | None = None

class Feature(ConfigSchema):
    page: bool | None = None # only this seems to be used everywhere
    
    # account
    event: bool | None = None
    profile: bool | None = None
    children: bool | None = None
    VACCINE_2: bool | None = None
    request: bool | None = None
    certificates: bool | None = None
    statements: bool | None = None
    agreement: bool | None = None
    reports: bool | None = None
    links_on_passport_family: bool | None = None
    documents_in_children: bool | None = None
    documents_in_profile: bool | None = None
    degustations: bool | None = None

    # events
    horizons_banner: bool | None = None
    news_list: bool | None = None

    # lessons
    lesson_tab: bool | None = None
    homework_tab: bool | None = None
    additional_tab: bool | None = None
    planned_result: bool | None = None
    average_mark: bool | None = None
    recommendations_service: bool | None = None

    class_results: bool | None = None # marks
    write_an_appeal: bool | None = None # test_works
    chats: bool | None = None # header
    personal_tutor: bool | None = None # subjects

    # schedule
    additional_lessons: bool | None = None
    additional_lessons_complaints: bool | None = None

    # PROJECT_WORKS
    task_cards: bool | None = None
    chat_card: bool | None = None
    marks_cards: bool | None = None
    materials_cards: bool | None = None

    feedback: bool | None = None # tutor

    # EXTERNAL_LINKS
    show_eais_oko_url: bool | None = None
    show_cashless_payment_for_meals_url: bool | None = None
    show_participation_in_olympiads_url: bool | None = None
    show_results_past_olympiads_url: bool | None = None

    period_view_mode: bool | None = None # rating

    # circles
    search_tab: bool | None = None
    favorites_tab: bool | None = None
    statements_tab: bool | None = None
    circles_tab: bool | None = None

class LabelNewConfigurations(ConfigSchema):
    final_marks: Feature | None = None
    test_works: Feature | None = None
    tutor: Feature | None = None
    about_school: Feature | None = None
    external_links: Feature | None = None
    exams: Feature | None = None
    subjects: Feature | None = None
    rating: Feature | None = None
    circles: Feature | None = None
    info_agreement: Feature | None = None

class FeatureFlags(ConfigSchema):
    about_school: Feature | None = None
    academic_debts: Feature | None = None
    account: Feature | None = None
    archives: Feature | None = None
    attendance: Feature | None = None
    events: Feature | None = None
    final_marks: Feature | None = None
    homeworks: Feature | None = None
    lessons: Feature | None = None
    marks: Feature | None = None
    test_works: Feature | None = None
    header: Feature | None = None
    subjects: Feature | None = None
    technical_works: Feature | None = None
    schedule: Feature | None = None
    info_agreement: Feature | None = None
    project_works: Feature | None = None
    exams: Feature | None = None
    tutor: Feature | None = None
    external_links: Feature | None = None
    rating: Feature | None = None
    circles: Feature | None = None

class ConfigType(Enum):
    diary = 'diary'
    unknown = 'unknown'

class BaseConfig(ConfigSchema):
    type: ConfigType | str | None = ConfigType.unknown

class DnevnikConfig(BaseConfig):
    type: ConfigType | str | None = ConfigType.diary
    base_stand_url: str | None = None
    dnevnik_stand_url: str | None = None
    library_stand_url: str = 'https://uchebnik.mos.ru'
    horizons_url: str | None = None
    school_stand_url: str | None = None
    stand_url_for_enable_ym: str | None = None
    material_launch_url: str | None = None
    school_stand_url_for_nsi: str | None = None
    school_stand_url_for_oge_ege: str | None = None
    consent_personal_data_processing_url: str | None = None
    consent_example_filling_form: str | None = None
    primakov_login_url: str | None = None
    app_version: str | None = None
    global_title: str | None = None
    global_description: str | None = None
    x_mes_subsystem: str | None = None
    primakov_school_id: list[int] | None = None
    time_in_minutes_to_save_cache: int | None = None
    time_in_minutes_to_save_cache_for_events: int | None = None
    time_in_minutes_to_save_cache_for_profile: int | None = None
    has_stand_info: int | None = None
    has_kfp: int | None = None
    is_region: int | None = None
    external_links: ExternalLinks | None = None
    api_urls: ApiURLs | None = None
    feature_flags: FeatureFlags | None = None
    label_new_configurations: LabelNewConfigurations | None = None

# endregion

#region other stuff

class Role(IdentifyableBase):
    title: str | None = None
    globalRoleTag: str | int | None = None

class SubsystemInfo(IdentifyableBase):
    title: str | None = None
    title_official: str | None = None
    url: str | None = None
    mnemonic: str | None = None
    description: str | None = None
    is_mobile: bool | None = None
    sort_order: int | None = None
    visible: bool | None = None

class Picture(BaseSchema):
    small: str | None = None # just a guess
    medium: str | None = None
    large: str | None = None

class EducationClass(NamedBase):
    uid: str | None = None
    education_stage_id: int | None = None
    parallel: NamedBase | None = None
    staff_ids: list[int] | None = None
    organization: GlobalNamedBase | None = None

class Education(BaseSchema):
    training_begin_at: datetime | None = None
    training_end_at: datetime | None = None
    class_: EducationClass | None = Field(default=None, alias='class')
    service_type: GlobalNamedBase | None = None

class UserInfo(BaseSchema):
    name: str | None = None
    mesh_id: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    middle_name: str | None = None
    gender: Gender | None = None
    agents: list[str] | None = None
    birth_date: datetime | None = None
    updated_at: datetime | None = None
    children: list[str] | None = None
    picture: Picture | None = None
    education: list[Education] | None = None

class MetricEntry(NamedBase):pass

#endregion

#region Sessions

class SessionProfile(IdentifyableBase):
    type: ProfileType | None = None
    roles: list[Any] | None = None
    agree_pers_data: bool | None = None
    school_id: int | None = None
    school_shortname: str | None = None
    subject_ids: list[int | Any] | None = None
    organization_id: str | int | None = None

class Sessions(UserInfoBase2):
    guid: str | None = None
    authentication_token: str | None = None
    person_id: UUID | str | None = None
    password_change_required: bool | None = None
    regional_auth: str | None = None
    profiles: list[SessionProfile] | None = None

#endregion

#region ProfileInfo

class School(BaseSchema):
    id: int | None = None
    global_school_id: int | None = None
    name: str | None = None
    short_name: str | None = None
    county: str | None = None
    principal: str | None = None
    phone: str | None = None
    municipal_unit_name: Any | str | None = None

class Group(BaseSchema):
    id: int | None = None
    name: str | None = None
    subject_id: int | None = None
    is_fake: bool | None = None

class Representative(UserInfoBase):
    person_id: str | None = None
    type_id: int | None = None
    type: str | None = None
    email: str | None = None

class Profile(UserInfoBase2):
    type: ProfileType | None = None
    contract_id: int | None = None
    email: str | None = None

class Child(Profile):
    class_name: str | None = None
    class_level_id: int | None = None
    class_unit_id: int | None = None
    age: int | None = None
    sudir_account_exists: bool | None = None
    sudir_login: Any | str | None = None
    is_legal_representative: bool | None = None
    parallel_curriculum_id: int | None = None
    contingent_guid: str | None = None
    enrollment_date: datetime | None = None
    service_type_id: int | None = None
    profession_specialty_code: Any | None = None
    profession_specialty_name: Any | None = None

    school: School | None = None
    groups: list[Group] | None = None
    representatives: list[Representative] | None = None
    sections: list[Group] | None = None

class ProfileInfo(BaseSchema):
    hash: str | None = None
    profile: Profile | None = None
    children: list[Child] | None = None

#endregion

#region Events

class EventSource(Enum):
    plan = 'PLAN'

class Event(IdentifyableBase):
    start_at: datetime | None = None
    finish_at: datetime | None = None
    source: EventSource | None = None
    source_id: int | None = None
    # these were null
    author_id: Any | None = None
    title: str | Any | None = None
    description: str | Any | None = None
    is_all_day: bool | Any | None = None
    conference_link: Any | None = None
    outdoor: bool | Any | None = None
    place: Any | None = None
    place_latitude: Any | None = None
    place_longitude: Any | None = None
    created_at: Any | None = None
    updated_at: Any | None = None
    attachments: Any | None = None
    author_name: str | Any | None = None
    registration_start_at: Any | None = None
    registration_end_at: Any | None = None
    place_name: Any | None = None
    contact_name: str | Any | None = None
    contact_phone: str | Any | None = None
    contact_email: str | Any | None = None
    comment: str | Any | None = None
    need_document: Any | None = None
    type: Any | None = None
    format_name: str | Any | None = None
    url: str | Any | None = None
    project_name: str | Any | None = None
    replaced_teacher_id: Any | None = None
    esz_field_id: Any | None = None
    course_lesson_type: Any | None = None
    lesson_form: Any | None = None
    lesson_education_type: Any | None = None
    activities: Any | None = None
    link_to_join: str | Any | None = None
    control: Any | None = None
    class_unit_ids: Any | None = None
    external_activities_type: Any | None = None
    address: Any | None = None
    place_comment: Any | None = None
    city_building_name: Any | None = None
    is_metagroup: Any | None = None
    absence_reason_id: Any | None = None
    nonattendance_reason_id: Any | None = None
    visible_fake_group: Any | None = None
    health_status: Any | None = None
    student_count: Any | None = None
    attendances: Any | None = None
    comment_count: Any | None = None
    comments: Any | None = None
    data: Any | None = None
    marks: Any | None = None
    stage: Any | None = None
    subjects: Any | None = None


#endregion



#region LIBRARY
#region Test info

class TestUseCase(Enum):
    preview = 'PREVIEW'
    homework = 'HOMEWORK'

class TestInfo(BaseSchema):
    title: str | Literal['Цифровое Домашнее Задание'] | None = None # that literal = anonymnous test (most likely), but better way to check is if use_case=UseCase.homework
    subject_ids: list[int] | None = None
    use_case: TestUseCase | None = None
    allowed_tries: int | None = None # 0 = infinite
    available_time_in_minutes: int | None = None
    task_total_count: int | None = None
    available_from: datetime | None = None
    available_until: datetime | None = None
    can_reanswer: bool | None = None
    answer_order_random: bool | None = None
    is_task_order_random: bool | None = None
    number_of_attempt: int | None = None
    last_attempt_id: int | None = None
    last_attempt_started_at: datetime | None = None

#endregion
#endregion