/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { BasicResponse } from '../models/BasicResponse';
import type { LoginAuthResponse } from '../models/LoginAuthResponse';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Login
     * @param username
     * @param password
     * @returns LoginAuthResponse Successful Response
     * @throws ApiError
     */
    public static loginLoginPost(
        username: string,
        password: string,
    ): CancelablePromise<LoginAuthResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/login',
            query: {
                'username': username,
                'password': password,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Logout
     * @returns any Successful Response
     * @throws ApiError
     */
    public static logoutLogoutPost(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/logout',
        });
    }
    /**
     * Signup
     * @param username
     * @param password
     * @param email
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static signupSignupPost(
        username: string,
        password: string,
        email: string,
    ): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/signup',
            query: {
                'username': username,
                'password': password,
                'email': email,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Confirm Signup
     * @param username
     * @param confirmationCode
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static confirmSignupConfirmSignupPost(
        username: string,
        confirmationCode: string,
    ): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/confirm-signup',
            query: {
                'username': username,
                'confirmation_code': confirmationCode,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Forgot Password
     * @param email
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static forgotPasswordForgotPasswordPost(
        email: string,
    ): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/forgot-password',
            query: {
                'email': email,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Verify Forgot Password
     * @param username
     * @param verificationCode
     * @param newPassword
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static verifyForgotPasswordVerifyForgotPasswordPost(
        username: string,
        verificationCode: string,
        newPassword: string,
    ): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/verify-forgot-password',
            query: {
                'username': username,
                'verification_code': verificationCode,
                'new_password': newPassword,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Change Password
     * @param accessToken
     * @param previousPassword
     * @param proposedPassword
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static changePasswordChangePasswordPost(
        accessToken: string,
        previousPassword: string,
        proposedPassword: string,
    ): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/change-password',
            query: {
                'access_token': accessToken,
                'previous_password': previousPassword,
                'proposed_password': proposedPassword,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Account
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static deleteAccountDeleteAccountPost(): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/delete-account',
        });
    }
    /**
     * Validate Access Token
     * @returns BasicResponse Successful Response
     * @throws ApiError
     */
    public static validateAccessTokenValidateTokenPost(): CancelablePromise<BasicResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/validate-token',
        });
    }
    /**
     * Protected Route
     * @returns any Successful Response
     * @throws ApiError
     */
    public static protectedRouteProtectedGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/protected',
        });
    }
}
