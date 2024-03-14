
from datetime import datetime

app_name = "kartoza_shop"
app_title = "Kartoza Shop"
app_publisher = "Kartoza"
app_description = "Enchance current e commerce sttings"
app_email = "juanique@kartoza.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kartoza_shop/css/kartoza_shop.css"
# app_include_js = "/assets/kartoza_shop/js/kartoza_shop.js"

# include js, css files in header of web template
web_include_css = f"/assets/kartoza_shop/css/main.css?v={datetime.now()}"
web_include_js = f"/assets/kartoza_shop/js/currency_session.js?v={datetime.now()}"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "kartoza_shop/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	# "get_shopping_cart_settings": "kartoza_shop.overrides.MultiCurrency.get_shopping_cart_settings",
	# "filters": "kartoza_shop.utils.jinja_filters"
}

# Installation
# ------------

# before_install = "kartoza_shop.install.before_install"
# after_install = "kartoza_shop.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "kartoza_shop.uninstall.before_uninstall"
# after_uninstall = "kartoza_shop.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "kartoza_shop.utils.before_app_install"
# after_app_install = "kartoza_shop.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "kartoza_shop.utils.before_app_uninstall"
# after_app_uninstall = "kartoza_shop.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kartoza_shop.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo"
    "E Commerce Settings": "kartoza_shop.overrides.MultiCurrency"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kartoza_shop.tasks.all"
# 	],
# 	"daily": [
# 		"kartoza_shop.tasks.daily"
# 	],
# 	"hourly": [
# 		"kartoza_shop.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kartoza_shop.tasks.weekly"
# 	],
# 	"monthly": [
# 		"kartoza_shop.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "kartoza_shop.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	# "frappe.desk.doctype.event.event.get_events": "kartoza_shop.event.get_events"
#     "erpnext.e_commerce.doctype.e_commerce_settings.get_shopping_cart_settings": "kartoza_shop.kartoza_shop.doctype"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "kartoza_shop.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["kartoza_shop.utils.before_request"]
# after_request = ["kartoza_shop.utils.after_request"]

# Job Events
# ----------
# before_job = ["kartoza_shop.utils.before_job"]
# after_job = ["kartoza_shop.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"kartoza_shop.auth.validate"
# ]
