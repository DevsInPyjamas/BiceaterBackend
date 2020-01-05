--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	!JNZ4A37KjMbxNKI7cjmxYlmRs9UrdpHPRwr1i5oQ	2019-12-12 10:27:20.917614+01	f	jesusparejo98	Jesús	Parejo Aliaga	jesusparejo98@gmail.com	f	t	2019-12-12 10:27:20.716855+01
2	pbkdf2_sha256$150000$t87Z3hjadSPe$kK0R4Rqq0K+SxQ0+hX08FWTDQ1TTn2B5W8SCQdmWh/k=	2019-12-12 19:26:53.101676+01	t	jesuspa98			jesusparejo98@gmail.com	t	t	2019-12-12 19:26:45.36171+01
5	pbkdf2_sha256$150000$Lzh1yu9fSVqp$Qy1o8t6H5x9s3rmjL55kt8dpJqPvPMt5Ad4K5PzNhMo=	\N	f	SamuJurado				f	t	2019-12-12 19:41:24.846327+01
6	pbkdf2_sha256$150000$Ewwn7JuorWHY$UHJDql9dzzQsBf7fVxVmj/IHiwWih3L/RKlovQ8ySeY=	\N	f	WanGarcia				f	t	2019-12-12 19:41:41.283257+01
4	pbkdf2_sha256$150000$hFkpXMj0JYyv$1RemKQIwZlfi/35Va0Y6R05M9G8MPsoABZZJ2ZOHEpA=	\N	f	PedroDiaz				f	t	2019-12-12 19:41:00+01
3	pbkdf2_sha256$150000$ml3p3vz4eVgr$2lpay2vZyJ2okHO1dLTBqF3tcz/Wo3r/E73Ove4D6ZU=	\N	f	Alek				f	t	2019-12-12 19:40:06+01
\.


--
-- Data for Name: BiceaterAPI_appuser; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public."BiceaterAPI_appuser" (user_id, "DoB", image, description, genre, hobbies) FROM stdin;
2	2019-12-12	../media/		M	
3	2019-12-12	../media/		M	
4	2019-12-12	../media/		M	
5	2019-12-12	../media/		M	
6	2019-12-12	../media/		M	
\.


--
-- Data for Name: BiceaterAPI_comment; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public."BiceaterAPI_comment" (comment_id, text, date, bike_hire_docking_station_id, answers_to_id, author_id) FROM stdin;
1	Spicy jalapeno bacon ipsum dolor amet meatball strip steak turducken, turkey ham hock hamburger jerky picanha chislic short loin cupim pork.	2019-12-12 19:44:50.606793+01	10	\N	2
2	Spicy jalapeno bacon ipsum dolor amet short ribs shoulder flank hamburger. Incididunt est chuck, shank nostrud turducken pork chop jowl.	2019-12-12 19:45:27.278112+01	11	\N	3
3	Salami pork belly dolore corned beef lorem adipisicing. Voluptate veniam occaecat consequat chuck. Short ribs chicken cillum kevin tri-tip c	2019-12-12 19:45:45.851933+01	12	\N	4
4	Rump dolor drumstick meatloaf, dolore excepteur doner est nulla kevin. Doner meatloaf fugiat bacon porchetta occaecat. Et tail bresaola meat	2019-12-12 19:46:04.218417+01	13	\N	5
5	Tri-tip ham hock rump ground round buffalo. Rump aliquip strip steak pork belly chuck in tempor shoulder eiusmod laboris consequat.	2019-12-12 19:46:25.974073+01	14	\N	6
6	Nisi porchetta fugiat burgdoggen adipisicing culpa consequat tail non tempor minim. Tenderloin tempor ut deserunt in adipisicing laboris.	2019-12-12 19:46:45.41441+01	14	\N	2
7	Jerky adipisicing cupim, ea kielbasa leberkas shankle. Leberkas reprehenderit burgdoggen, biltong ullamco frankfurter ut irure.	2019-12-12 19:47:08.206023+01	13	\N	3
8	Aliquip hamburger spare ribs magna beef picanha eiusmod, ground round adipisicing pancetta venison est non. Shank laborum nisi kevin.	2019-12-12 19:47:36.748736+01	12	\N	5
9	Irure chuck sausage dolore sunt prosciutto deserunt rump shank. Brisket ribeye corned beef laboris, jerky cupidatat pancetta reprehenderit.	2019-12-12 19:47:54.267852+01	11	\N	4
10	Pork loin short ribs boudin eu corned beef. Andouille brisket jerky, elit tongue magna velit short loin id beef ribs in veniam frankfurter.	2019-12-12 19:48:10.77416+01	10	\N	6
11	Spicy jalapeno bacon ipsum dolor amet ex strip steak drumstick, andouille spare ribs et tail turducken nulla in sint leberkas excepteur.	2019-12-12 19:52:45.355204+01	10	1	3
12	Sunt culpa kevin, turkey deserunt pork belly hamburger fatback capicola dolore beef aliqua. Et occaecat t-bone frankfurter, chuck kevin.	2019-12-12 19:53:08.162456+01	14	6	5
13	Short ribs doner elit exercitation, ribeye enim brisket cupim tri-tip commodo shank rump velit landjaeger. Meatloaf incididunt ham, labore.	2019-12-12 19:53:33.275115+01	11	2	2
14	Aliqua pig meatball proident officia brisket swine cow est sint excepteur pancetta. Quis tongue pork chop landjaeger pariatur buffalo ball.	2019-12-12 19:53:53.900902+01	13	7	4
15	Deserunt tempor prosciutto beef ribs ipsum laborum, andouille labore t-bone chicken tenderloin buffalo in. Duis id aute ut irure hamburger.	2019-12-12 19:57:31.004093+01	12	3	6
16	Pariatur culpa fugiat tongue frankfurter eu. Est velit ullamco pork belly ea consequat aute brisket beef ribs id reprehenderit.	2019-12-12 19:57:53.078189+01	11	9	3
17	Rump short ribs consequat veniam, doner occaecat dolor ut ea pork belly. Pork ipsum aliqua incididunt ullamco chislic, ham in capicola short	2019-12-12 19:58:28.448893+01	13	4	2
18	Consectetur consequat kielbasa ham hock prosciutto andouille chuck, non irure ribeye ullamco. Kevin rump ex, deserunt biltong beef ham hock.	2019-12-12 19:58:47.585877+01	12	8	4
19	Nisi nostrud ut, leberkas strip steak rump duis chicken sirloin pariatur chislic in venison salami. Landjaeger ham hock swine, pig picanha.	2019-12-12 20:01:41.24453+01	14	5	5
20	Tongue short loin corned beef sirloin pork loin proident bresaola non tri-tip shoulder aliquip. Dolor sunt brisket biltong, fatback non.	2019-12-12 20:02:08.321721+01	10	10	4
\.


--
-- Data for Name: BiceaterAPI_rating; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public."BiceaterAPI_rating" (rating_id, rating, date, bike_hire_docking_station_id, author_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	social_django	association
8	social_django	code
9	social_django	nonce
10	social_django	usersocialauth
11	social_django	partial
12	BiceaterAPI	appuser
13	BiceaterAPI	rating
14	BiceaterAPI	comment
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add association	7	add_association
26	Can change association	7	change_association
27	Can delete association	7	delete_association
28	Can view association	7	view_association
29	Can add code	8	add_code
30	Can change code	8	change_code
31	Can delete code	8	delete_code
32	Can view code	8	view_code
33	Can add nonce	9	add_nonce
34	Can change nonce	9	change_nonce
35	Can delete nonce	9	delete_nonce
36	Can view nonce	9	view_nonce
37	Can add user social auth	10	add_usersocialauth
38	Can change user social auth	10	change_usersocialauth
39	Can delete user social auth	10	delete_usersocialauth
40	Can view user social auth	10	view_usersocialauth
41	Can add partial	11	add_partial
42	Can change partial	11	change_partial
43	Can delete partial	11	delete_partial
44	Can view partial	11	view_partial
45	Can add app user	12	add_appuser
46	Can change app user	12	change_appuser
47	Can delete app user	12	delete_appuser
48	Can view app user	12	view_appuser
49	Can add rating	13	add_rating
50	Can change rating	13	change_rating
51	Can delete rating	13	delete_rating
52	Can view rating	13	view_rating
53	Can add comment	14	add_comment
54	Can change comment	14	change_comment
55	Can delete comment	14	delete_comment
56	Can view comment	14	view_comment
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-12-12 19:40:06.264038+01	3	alkasete	1	[{"added": {}}]	4	2
2	2019-12-12 19:41:00.123473+01	4	pedroDiaz	1	[{"added": {}}]	4	2
3	2019-12-12 19:41:24.946776+01	5	SamuJurado	1	[{"added": {}}]	4	2
4	2019-12-12 19:41:41.388905+01	6	WanGarcia	1	[{"added": {}}]	4	2
5	2019-12-12 19:42:07.003218+01	4	PedroDiaz	2	[{"changed": {"fields": ["username"]}}]	4	2
6	2019-12-12 19:42:21.038064+01	3	Alek	2	[{"changed": {"fields": ["username"]}}]	4	2
7	2019-12-12 19:42:39.064585+01	2	jesuspa98: 2	1	[{"added": {}}]	12	2
8	2019-12-12 19:42:50.063734+01	3	Alek: 3	1	[{"added": {}}]	12	2
9	2019-12-12 19:42:58.050616+01	4	PedroDiaz: 4	1	[{"added": {}}]	12	2
10	2019-12-12 19:43:07.033549+01	5	SamuJurado: 5	1	[{"added": {}}]	12	2
11	2019-12-12 19:43:18.424955+01	6	WanGarcia: 6	1	[{"added": {}}]	12	2
12	2019-12-12 19:44:50.609163+01	1	jesuspa98: 1	1	[{"added": {}}]	14	2
13	2019-12-12 19:45:27.280327+01	2	Alek: 2	1	[{"added": {}}]	14	2
14	2019-12-12 19:45:45.865726+01	3	PedroDiaz: 3	1	[{"added": {}}]	14	2
15	2019-12-12 19:46:04.221436+01	4	SamuJurado: 4	1	[{"added": {}}]	14	2
16	2019-12-12 19:46:25.975766+01	5	WanGarcia: 5	1	[{"added": {}}]	14	2
17	2019-12-12 19:46:45.422186+01	6	jesuspa98: 6	1	[{"added": {}}]	14	2
18	2019-12-12 19:47:08.207852+01	7	Alek: 7	1	[{"added": {}}]	14	2
19	2019-12-12 19:47:36.752585+01	8	SamuJurado: 8	1	[{"added": {}}]	14	2
20	2019-12-12 19:47:54.269645+01	9	PedroDiaz: 9	1	[{"added": {}}]	14	2
21	2019-12-12 19:48:10.78018+01	10	WanGarcia: 10	1	[{"added": {}}]	14	2
22	2019-12-12 19:52:45.357842+01	11	Alek: 11	1	[{"added": {}}]	14	2
23	2019-12-12 19:53:08.166308+01	12	SamuJurado: 12	1	[{"added": {}}]	14	2
24	2019-12-12 19:53:33.276675+01	13	jesuspa98: 13	1	[{"added": {}}]	14	2
25	2019-12-12 19:53:53.90798+01	14	PedroDiaz: 14	1	[{"added": {}}]	14	2
26	2019-12-12 19:57:31.005587+01	15	WanGarcia: 15	1	[{"added": {}}]	14	2
27	2019-12-12 19:57:53.082105+01	16	Alek: 16	1	[{"added": {}}]	14	2
28	2019-12-12 19:58:28.45482+01	17	jesuspa98: 17	1	[{"added": {}}]	14	2
29	2019-12-12 19:58:47.592589+01	18	PedroDiaz: 18	1	[{"added": {}}]	14	2
30	2019-12-12 20:01:41.246353+01	19	SamuJurado: 19	1	[{"added": {}}]	14	2
31	2019-12-12 20:02:08.323197+01	20	PedroDiaz: 20	1	[{"added": {}}]	14	2
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-12-12 10:14:27.711733+01
2	contenttypes	0002_remove_content_type_name	2019-12-12 10:14:27.767252+01
3	auth	0001_initial	2019-12-12 10:14:28.115143+01
4	auth	0002_alter_permission_name_max_length	2019-12-12 10:14:28.668708+01
5	auth	0003_alter_user_email_max_length	2019-12-12 10:14:28.684663+01
6	auth	0004_alter_user_username_opts	2019-12-12 10:14:28.697748+01
7	auth	0005_alter_user_last_login_null	2019-12-12 10:14:28.707728+01
8	auth	0006_require_contenttypes_0002	2019-12-12 10:14:28.718018+01
9	auth	0007_alter_validators_add_error_messages	2019-12-12 10:14:28.732249+01
10	auth	0008_alter_user_username_max_length	2019-12-12 10:14:28.798061+01
11	auth	0009_alter_user_last_name_max_length	2019-12-12 10:14:28.834075+01
12	auth	0010_alter_group_name_max_length	2019-12-12 10:14:28.861426+01
13	auth	0011_update_proxy_permissions	2019-12-12 10:14:28.882061+01
14	BiceaterAPI	0001_initial	2019-12-12 10:14:29.14248+01
15	admin	0001_initial	2019-12-12 10:14:29.361126+01
16	admin	0002_logentry_remove_auto_add	2019-12-12 10:14:29.473657+01
17	admin	0003_logentry_add_action_flag_choices	2019-12-12 10:14:29.498361+01
18	sessions	0001_initial	2019-12-12 10:14:29.569264+01
19	default	0001_initial	2019-12-12 10:14:30.042953+01
20	social_auth	0001_initial	2019-12-12 10:14:30.046085+01
21	default	0002_add_related_name	2019-12-12 10:14:30.205026+01
22	social_auth	0002_add_related_name	2019-12-12 10:14:30.206216+01
23	default	0003_alter_email_max_length	2019-12-12 10:14:30.216825+01
24	social_auth	0003_alter_email_max_length	2019-12-12 10:14:30.218242+01
25	default	0004_auto_20160423_0400	2019-12-12 10:14:30.234373+01
26	social_auth	0004_auto_20160423_0400	2019-12-12 10:14:30.235951+01
27	social_auth	0005_auto_20160727_2333	2019-12-12 10:14:30.285913+01
28	social_django	0006_partial	2019-12-12 10:14:30.396493+01
29	social_django	0007_code_timestamp	2019-12-12 10:14:30.491936+01
30	social_django	0008_partial_timestamp	2019-12-12 10:14:30.542365+01
31	social_django	0003_alter_email_max_length	2019-12-12 10:14:30.590696+01
32	social_django	0005_auto_20160727_2333	2019-12-12 10:14:30.597709+01
33	social_django	0001_initial	2019-12-12 10:14:30.606307+01
34	social_django	0002_add_related_name	2019-12-12 10:14:30.614803+01
35	social_django	0004_auto_20160423_0400	2019-12-12 10:14:30.624082+01
36	BiceaterAPI	0002_auto_20191212_1838	2019-12-12 19:38:21.331306+01
37	BiceaterAPI	0003_auto_20191212_1854	2019-12-12 19:54:51.455439+01
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
iy4ythq1enuoa45z8gvpfib3ec9nr79p	OWMxNDJlZDkyMjdhY2ZlOTI4NTNjNWExODMxYzZiMTEzN2U3NmYyYTp7Imdvb2dsZS1vYXV0aDJfc3RhdGUiOiJZSmM1YktTRWxuZDR1MDh3TTNWaWVHenJ5M0JTbUNaVSIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ29vZ2xlLkdvb2dsZU9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6ImRiYTAyZGZiMGFkYzc5NTY2MmM3N2I1MDI0ZTY2YTY2MjAzYWU3MTUiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnb29nbGUtb2F1dGgyIn0=	2019-12-26 10:27:20.940947+01
rvmv2zezl4u1vqpk234j4exygjg0k81k	YmE5MTFmMWMzZmRkYmZlZjhiNzZmMDI4NGMwZTA4ZDRlMGJlMjQyZjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOTU3NDkxNzg3ZWIzYWNiMTcxY2MyNzE5YTk4M2EyNzg2ODc5MjllIn0=	2019-12-26 19:26:53.109342+01
\.


--
-- Data for Name: social_auth_association; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.social_auth_association (id, server_url, handle, secret, issued, lifetime, assoc_type) FROM stdin;
\.


--
-- Data for Name: social_auth_code; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.social_auth_code (id, email, code, verified, "timestamp") FROM stdin;
\.


--
-- Data for Name: social_auth_nonce; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.social_auth_nonce (id, server_url, "timestamp", salt) FROM stdin;
\.


--
-- Data for Name: social_auth_partial; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.social_auth_partial (id, token, next_step, backend, data, "timestamp") FROM stdin;
\.


--
-- Data for Name: social_auth_usersocialauth; Type: TABLE DATA; Schema: public; Owner: DiP
--

COPY public.social_auth_usersocialauth (id, provider, uid, extra_data, user_id) FROM stdin;
1	google-oauth2	jesusparejo98@gmail.com	{"expires": 3600, "auth_time": 1576142840, "token_type": "Bearer", "access_token": "ya29.Il-0B94h-Xbjv84-KoXtnShlyEbuUWJFel7wOzqGr4FRml-z6fcVHdAHi7LpUr8U4cMdG9RYJBl6j57A-15RkC8CjFrXNst2G6ejg-dpV8KpwU7hZfqgm6oVtCOpPet3IA"}	1
\.


--
-- Name: BiceaterAPI_comment_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public."BiceaterAPI_comment_comment_id_seq"', 20, true);


--
-- Name: BiceaterAPI_rating_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public."BiceaterAPI_rating_rating_id_seq"', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 56, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 6, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 31, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 37, true);


--
-- Name: social_auth_association_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.social_auth_association_id_seq', 1, false);


--
-- Name: social_auth_code_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.social_auth_code_id_seq', 1, false);


--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.social_auth_nonce_id_seq', 1, false);


--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.social_auth_partial_id_seq', 1, false);


--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: DiP
--

SELECT pg_catalog.setval('public.social_auth_usersocialauth_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--

