import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ssm from 'aws-cdk-lib/aws-ssm';

export class SsmStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);
        
        new ssm.StringParameter(this, 'TestParameter', {
            parameterName: '/my/test/parameter',
            stringValue: 'This is a test parameter',
        });
    }
}

const app = new cdk.App();
new SsmStack(app, 'SsmStack');