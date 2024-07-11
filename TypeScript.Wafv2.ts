import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';

export class WafStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        new wafv2.CfnWebACL(this, 'TestWebACL', {
            defaultAction: { allow: {} },
            scope: 'REGIONAL',
            visibilityConfig: {
                sampledRequestsEnabled: true,
                cloudWatchMetricsEnabled: true,
                metricName: 'testMetric',
            },
            name: 'TestWebACL',
            rules: [
                {
                    name: 'BlockIPRule',
                    priority: 1,
                    action: { block: {} },
                    visibilityConfig: {
                        sampledRequestsEnabled: true,
                        cloudWatchMetricsEnabled: true,
                        metricName: 'blockIPMetric',
                    },
                    statement: {
                        ipSetReferenceStatement: {
                            arn: 'arn:aws:wafv2:region:account-id:regional/ipset/ip-set-id',
                        },
                    },
                },
            ],
        });
    }
}

const app = new cdk.App();
new WafStack(app, 'WafStack');