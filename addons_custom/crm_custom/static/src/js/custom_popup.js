odoo.define('crm_custom.custom_popup', function (require) {
    'use strict';

    const AbstractAction = require('web.AbstractAction');
    const core = require('web.core');
    const Dialog = require('web.Dialog');
    const rpc = require('web.rpc');

    const _t = core._t;

    // Định nghĩa một action để mở popup
    const CustomPopup = AbstractAction.extend({
        // Hàm khởi tạo
        start: function () {
            this._super.apply(this, arguments);
            this.openPopup();
        },

        // Hàm mở popup
        openPopup: function () {
            const self = this;
            
            // Gọi RPC để lấy dữ liệu từ model crm.lead
            rpc.query({
                model: 'crm.lead',
                method: 'search_read',
                args: [[], ['name', 'user_id', 'team_id', 'create_date', 'min_revenue']], // Lấy các trường name, email_from và phone
            }).then(function (leads) {
                // Tạo nội dung cho popup
                let content = '<div class="o_lead_popup"><table class="table table-bordered"><thead><tr><th>Name</th><th>user_id</th><th>create_date</th><th>min_revenue</th></tr></thead><tbody>';
                leads.forEach(function (lead) {
                    content += `<tr><td>${lead.name || ''}</td><td>${lead.user_id || ''}</td><td>${lead.team_id || ''}</td><td>${lead.create_date || ''}</td><td>${lead.min_revenue || ''}</td></tr>`;
                });
                content += '</tbody></table></div>';

                // Mở dialog với nội dung đã tạo
                Dialog.alert(self, content, {
                    title: _t('Leads List'),
                    size: 'large',
                });
            });
        },
    });

    // Đăng ký action
    core.action_registry.add('custom_popup', CustomPopup);
});
